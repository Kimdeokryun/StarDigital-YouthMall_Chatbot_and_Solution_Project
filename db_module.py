import pymysql as mysql


def connect_and_query():
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

    return conn, cursor

# 넘버링 id 값에 따른 정보 찾기
def search_chat_information(bot_message):
    conn, cursor = connect_and_query()

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
            'id': bot_message,
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

# 다음 번호 아이템 찾기
def search_other_item(item_id):
    conn, cursor = connect_and_query()

    # response 테이블에서 정보 찾기
    cursor.execute("SELECT information, button, image FROM response WHERE _id = %s", (str(int(item_id)+1),))
    response_data = cursor.fetchone()

    # imageurl 테이블에서 정보 찾기
    cursor.execute("SELECT url FROM imageurl WHERE id = %s", (str(int(item_id)+1),))
    image_data = cursor.fetchone()

    # mall 테이블에서 정보 찾기
    cursor.execute("SELECT item, name FROM mall WHERE id = %s", (str(int(item_id) + 1),))
    mall_data = cursor.fetchone()
    conn.close()

    # 결과를 딕셔너리 형태로 반환
    return {
        'response': {
            'id': str(int(item_id)+1),
            'information': response_data[0] if response_data else None,
            'button': response_data[1] if response_data else None,
            'image': response_data[2] if response_data else None,
            'url': image_data[0] if image_data else None,
            'item': {
                'name': mall_data[1] if mall_data else None,
                'image': image_data[0] if image_data else None,
                'url': image_data[0] if image_data else None
            } if mall_data else None
        }
    }

# 다음 번호 업체명 찾기
def search_mall():
    conn, cursor = connect_and_query()

    # mall 테이블에서 정보 찾기
    cursor.execute("SELECT DISTINCT name FROM mall")
    mall_data = cursor.fetchall()
    conn.close()

    print(mall_data)

    # 결과를 " | "로 구분하여 출력 (버튼형을 위함)
    mall_names = " | ".join([name[0] for name in mall_data])
    print(mall_names)

    return {
        'response': {
            'id': None,
            'information': None,
            'button': mall_names if mall_data else None,
            'image': None,
            'url': None,
            'item': None
        }
    }



