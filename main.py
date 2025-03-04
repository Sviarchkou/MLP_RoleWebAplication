from __init__ import create_app
#from testFlask import *
# from models import models
# from auth import auth

if __name__ == '__main__':
    create_app().run()








#from flask import Flask, jsonify, request
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


#
# app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'your-secret-key'
# jwt = JWTManager(app)
#
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.json.get('username')
#     password = request.json.get('password')
#     # Простейшая проверка (в реальном приложении - поиск в базе данных)
#     if username == 'admin' and password == 'secret':
#         token = create_access_token(identity=username)
#         return jsonify(access_token=token)
#     return jsonify({"msg": "Неверные учетные данные"}), 401
#
# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
#
# if __name__ == '__main__':
#     app.run()
