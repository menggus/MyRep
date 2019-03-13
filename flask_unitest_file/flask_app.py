from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['post'])
def login():
    """简单登录demo"""
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username, password]):
        res = {
            'code': 1,
            'message': "need all data"
        }
        return jsonify(res)
    if username == "admin" and password == "123456":  # 简化，自行设定账密
        res = {
            'code': 0,
            'message': "login success"
        }
        return jsonify(res)
    else:
        res = {
            'code': 2,
            'message': "login infos error"
        }
        return jsonify(res)


if __name__ == '__main__':
    app.run()
