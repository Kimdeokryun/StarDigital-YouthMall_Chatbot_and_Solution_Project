import pymysql as mysql


def connect_and_query(bot_message):

    # 데이터베이스에 연결
    db_config = {
        'host': '',
        'user': '',
        'password': '',
        'database': ''
    }

    # 데이터베이스 연결
    conn = mysql.connect(**db_config)
    cursor = conn.cursor()

    # response 테이블에서 정보 찾기
    cursor.execute("SELECT information, button, image FROM response WHERE _id = %s", (bot_message,))
    response_data = cursor.fetchone()

    # imageurl 테이블에서 정보 찾기
    cursor.execute("SELECT url FROM imageurl WHERE id = %s", (bot_message,))
    image_data = cursor.fetchone()

    if int(bot_message) > 100:
        # mall 테이블에서 정보 찾기
        cursor.execute("SELECT item, name FROM mall WHERE id = %s", (bot_message,))
        mall_data = cursor.fetchone()
        conn.close()
    else:
        mall_data = None

    # 결과를 딕셔너리 형태로 반환
    return {
        'response': {
            'information': response_data[0],
            'button': response_data[1],
            'image': response_data[2],
            'url': image_data[0] if image_data else None,
            'item': {
                'name': mall_data[1] if mall_data else None,
                'image': image_data[0] if image_data else None,
                'url': image_data[0] if image_data else None
            } if mall_data else None
        }
    }