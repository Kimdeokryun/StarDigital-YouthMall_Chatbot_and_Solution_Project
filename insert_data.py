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
df = pd.read_excel(excel_file, sheet_name="챗봇 답변 구성")

# 데이터베이스 연결
conn = mysql.connect(**db_config)
cursor = conn.cursor()


def process_nan(value):
    return value if pd.notnull(value) else ""


# 엑셀 데이터를 데이터베이스에 입력하는 함수
def insert_data(row):
    insert_response_query = "INSERT INTO response (_id, information, button, image) VALUES (%s, %s, %s, %s)"
    response_id = int(row[0])
    cursor.execute(insert_response_query, (response_id, process_nan(row[1]), process_nan(row[2]), process_nan(row[3])))

    if pd.notnull(row[4]):
        insert_image_query = "INSERT INTO imageurl (id, url) VALUES (%s, %s)"
        cursor.execute(insert_image_query, (response_id, process_nan(row[4])))

    if pd.notnull(row[5]) or pd.notnull(row[6]):
        insert_mall_query = "INSERT INTO mall (id, item, name) VALUES (%s, %s, %s)"
        cursor.execute(insert_mall_query, (response_id, process_nan(row[5]), process_nan(row[6])))


# 엑셀 데이터를 순회하며 데이터베이스에 입력
for _, row in df.iterrows():
    insert_data(row)

# 변경 사항 저장 및 연결 종료
conn.commit()
conn.close()

print("Data inserted successfully.")
