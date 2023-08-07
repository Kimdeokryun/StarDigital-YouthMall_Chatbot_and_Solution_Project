from flask import Flask, request, jsonify
import db_module# 예시로 데이터베이스와 연동하는 모듈
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/find_response', methods=['POST'])
def find_response():
    data = request.get_json()
    print(data)
    bot_message = data['botMessage']

    # 데이터베이스와 연동하여 응답 생성 (예시)
    response_from_database = db_module.connect_and_query(bot_message)
    print(response_from_database)
    return jsonify(responseFromDatabase=response_from_database)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)