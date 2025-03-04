from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, set_access_cookies
from forms.user_creation_form import UserCreationFrom
from models.role import Role
from extensions import db, bcrypt, jwt
# from flask_login import login_user, logout_user
from models.user import User

# from app.forms.user_creation_form import UserCreationFrom


auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/auth', methods=['POST', 'GET'])
def authorization():
    if request.method == 'GET':
        return render_template("auth.html")
    return login()


@auth_bp.route('/login', methods=['POST'])
def login():
    # username = request.form['username']
    # password = request.form['password']

    login = request.json.get('login')
    password = request.json.get('password')

    user = User.query.filter_by(login=login).first()
    if user and bcrypt.check_password_hash(user.password, password):
        token = create_access_token(identity=login)
        response = jsonify({'message': 'Logged in'})
        set_access_cookies(response, token)
        # response.set_access_cookies(
        #     'jwt',  # Имя куки
        #     token,  # Значение куки
        #     httponly=True,  # Флаг HttpOnly
        #     secure=True,  # Только для HTTPS
        #     samesite='Strict',  # Защита от CSRF
        #     max_age=30 * 60  # Срок действия куки (30 минут)
        # )
        return response
        #return jsonify(access_token=token)
    else:
        return jsonify({"msg": "Неверные учетные данные"}), 401


@auth_bp.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserCreationFrom()
    if request.method == 'GET':
        return render_template("create_user.html", form=form)
    if form.validate_on_submit():
        return sign_in(form=form)
    else:
        print("Error in reg")
    return render_template("create_user.html", form=form)


@auth_bp.route('/sign_in', methods=['POST'])
def sign_in(form):
    name = request.form['name']
    login = request.form['login']
    password_hash = bcrypt.generate_password_hash(form.password.data).decode("UTF-8")

    if User.query.filter_by(login=login).first():
        return "Пользователь с таким именем/логином уже существует"
    role_name = request.form['role']
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        try:
            role = Role(name=role_name)
            db.session.add(role)
            db.session.commit()
            role = Role.query.filter_by(name=role.name).first()
        except Exception as ex:
            print("DB exeption in Role")
            print(ex)
    role_id = role.id
    personal_number = request.form['personal_number']
    residency = request.form['residency']
    phone = request.form['phone']

    user = User(name=name,
                login=login,
                password=password_hash,
                role_id=role_id,
                personal_number=personal_number,
                residency=residency,
                phone=phone)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as ex:
        print("DB exeption in User")
        print(ex)

    return jsonify({'message': 'User is created'})


@auth_bp.route('/logout', methods=['POST', 'GET'])
def logout():
    # logout_user()
    return redirect("/auth")


@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
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
