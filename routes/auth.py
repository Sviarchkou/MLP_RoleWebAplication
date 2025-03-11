from flask import Blueprint, render_template, request, redirect, jsonify, make_response, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies, jwt_required

import models.user
from extensions import bcrypt, db
from models.role import Role
from models.user import User


auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth', methods=['POST', 'GET'])
def authorization():
    if request.method == 'GET':
        return render_template("auth.html")
    return login()


@auth_bp.route('/login', methods=['POST'])
def login():
    login = request.json.get('login')
    password = request.json.get('password')
    user = db.session.query(User).filter_by(login=login).join(Role).first()
    # user = User.query.filter_by(login=login).first()
    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity=login)
        response = jsonify({'message': 'Logged in'})
        set_access_cookies(response, token)
        return response
    else:
        return make_response("Wrong data", 401)


@auth_bp.route('/<int:id>/logout', methods=['GET'])
def logout(id):
    return redirect(url_for('auth_bp.authorization'))


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    models.user.current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# from init import app
# from flask import render_template, request, jsonify, redirect
# #from flask_jwt import JWT, create_access_token, jwt_required, get_jwt_identity
#
# @app.route('/auth', methods=['POST', 'GET'])
# def authorization():
#     if request.method == 'GET':
#         return render_template("auth.html")
#     return login()
#
#
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#
#     # Простейшая проверка (в реальном приложении - поиск в базе данных)
#     if username == 'admin' and password == 'secret':
#         token = create_access_token(identity=username)
#         return jsonify(access_token=token)
#     return jsonify({"msg": "Неверные учетные данные"}), 401
#
#
# @app.route('/reg', methods=['POST', 'GET'])
# def registration():
#     if request.method == 'GET':
#         return render_template("reg.html")
#     return redirect("/signIn")
#
#
# @app.route('/signIn', methods=['POST'])
# def reg():
#     username = request.json.get('username')
#     password = request.json.get('password')
#
#     if username == 'admin' and password == 'secret':
#         token = create_access_token(identity=username)
#         redirect("/home")
#         return jsonify(access_token=token)
#     return jsonify({"msg": "Неверные учетные данные"}), 401
#
# #
# # @app.route('/protected', methods=['GET'])
# # @jwt_required()
# # def protected():
# #     current_user = get_jwt_identity()
# #     return jsonify(logged_in_as=current_user), 200
#
