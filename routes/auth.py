from flask import Blueprint, render_template, request, redirect
from ..extensions import db
# from flask_login import login_user, logout_user
# from app.models.user import User
# from app.forms.user_creation_form import UserCreationFrom


auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth', methods=['POST', 'GET'])
def authorization():
    if request.method == 'GET':
        return render_template("auth.html")
    return login()


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    # Простейшая проверка (в реальном приложении - поиск в базе данных)
    if user and user.password == password:
        print("good")
        # login_user(user)
        return redirect("/home")
    else:
        return redirect("/")


@auth_bp.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        return render_template("reg.html")
    # form = UserCreationFrom()
    # if form.validate_on_submit():
    #     return sign_in()
    # else:
    #     print("Error in reg")
    #     # return sign_in()


@auth_bp.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'secret':
        print("good")
        return redirect("/home")
    else:
        print("bad")
        return redirect("/")


@auth_bp.route('/logout', methods=['POST', 'GET'])
def logout():
    #logout_user()
    return redirect("/auth")



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
