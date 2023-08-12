from flask import Flask, request, jsonify, render_template, redirect
import db_module    # 예시로 데이터베이스와 연동하는 모듈
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template("Main.html")


@app.route('/index')
def index2():
    return redirect("/")

@app.route('/chat', methods=['GET'])
def chat():
    val = request.args
    get_type = val.get("type")

    if get_type == None or get_type == "0":
        get_type = "0"
    elif get_type == "1":
        get_type = "1"
    else:
        get_type = "-1"
    return render_template("Chat.html", get_type=get_type)


@app.route('/review')
def review():
    return render_template("Review.html")


@app.route('/api/find_response', methods=['POST'])
def find_response():
    data = request.get_json()
    bot_message = data['botMessage']

    # 데이터베이스와 연동하여 응답 생성 (예시)
    response_from_database = db_module.search_chat_information(bot_message)
    print(response_from_database)
    return jsonify(response_from_database)


@app.route('/api/other_item', methods=['POST'])
def other_item():
    data = request.get_json()
    before_id = data['id']

    # 데이터베이스와 연동하여 응답 생성 (예시)
    response_from_database = db_module.search_other_item(before_id)
    print(response_from_database)
    return jsonify(response_from_database)


@app.route('/api/search_mall', methods=['POST'])
def search_mall():

    # 데이터베이스와 연동하여 응답 생성 (예시)
    response_from_database = db_module.search_mall()
    return jsonify(response_from_database)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)