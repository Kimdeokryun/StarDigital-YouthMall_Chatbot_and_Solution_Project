import pandas as pd
import pymysql as mysql

# AWS RDS MySQL 연결 정보
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

# 엑셀 파일 읽기
excel_file = '.xlsx'
df = pd.read_excel(excel_file)


# NaN 값을 공백으로 처리하는 함수
def process_nan(value):
    return value if pd.notnull(value) else ""


# 데이터베이스 연결
conn = mysql.connect(**db_config)
cursor = conn.cursor()


# 엑셀 데이터를 데이터베이스에 업데이트 또는 삽입하는 함수
def upsert_data(row):
    response_id = row[0]
    select_query = "SELECT _id FROM response WHERE _id = %s"
    cursor.execute(select_query, (response_id,))
    existing_id = cursor.fetchone()

    if existing_id:
        update_response_query = "UPDATE response SET information = %s, button = %s, image = %s WHERE _id = %s"
        processed_row = (process_nan(row[1]), process_nan(row[2]), process_nan(row[3]), response_id)
        cursor.execute(update_response_query, processed_row)

        if pd.notnull(row[4]):
            update_image_query = "UPDATE imageurl SET url = %s WHERE id = %s"
            cursor.execute(update_image_query, (row[4], response_id))

        if pd.notnull(row[5]) or pd.notnull(row[6]):
            update_mall_query = "UPDATE mall SET item = %s, name = %s WHERE id = %s"
            cursor.execute(update_mall_query, (process_nan(row[5]), process_nan(row[6]), response_id))
    else:
        insert_response_query = "INSERT INTO response (_id, information, button, image) VALUES (%s, %s, %s, %s)"
        processed_row = (response_id, process_nan(row[1]), process_nan(row[2]), process_nan(row[3]))
        cursor.execute(insert_response_query, processed_row)

        if pd.notnull(row[4]):
            insert_image_query = "INSERT INTO imageurl (id, url) VALUES (%s, %s)"
            cursor.execute(insert_image_query, (response_id, row[4]))

        if pd.notnull(row[5]) or pd.notnull(row[6]):
            insert_mall_query = "INSERT INTO mall (id, item, name) VALUES (%s, %s, %s)"
            cursor.execute(insert_mall_query, (response_id, process_nan(row[5]), process_nan(row[6])))


# 엑셀 데이터를 순회하며 데이터베이스에 업데이트 또는 삽입
for _, row in df.iterrows():
    upsert_data(row)

# 변경 사항 저장 및 연결 종료
conn.commit()
conn.close()

print("Data upserted successfully.")