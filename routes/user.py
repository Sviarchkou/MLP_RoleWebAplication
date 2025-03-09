from flask import Blueprint, render_template, request, redirect, jsonify, flash

from forms.password_change_form import PasswordChangeForm
from forms.user_creation_form import UserCreationFrom
from forms.user_edit_form import UserEditFrom
from models.role import Role
from extensions import db, bcrypt
from models.user import User


user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserCreationFrom()
    if request.method == 'POST':
        if form.validate_on_submit():
            add_user(form=form)
        else:
            flash('Form is invalid', "warning")
        return redirect("/home")
    return render_template("user/create_user.html", form=form)


def add_user(form):
    name = request.form['name']
    login = request.form['login']
    password_hash = bcrypt.generate_password_hash(form.password.data).decode("UTF-8")

    if User.query.filter_by(login=login).first():
        flash("Пользователь с таким именем/логином уже существует", "warning")
        return

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

    # flash('User is created', "success")



@user_bp.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit_user(id):
    user = User.query.get(id)
    if not user:
        flash("No such user")
        return redirect("/home")

    form = UserEditFrom()
    if request.method == 'POST':
        if form.validate_on_submit():
            update_user(user=user)
            redirect("/home")
        else:
            flash('Form is invalid', "warning")
    return render_template("user/edit_user.html", form=form, user=user)


def update_user(user: User):
    name = request.form['name']
    login = request.form['login']

    if login != user.login:
        if User.query.filter_by(login=login).first():
            flash("Пользователь с таким именем/логином уже существует", "warning")
            return

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

    user.name = name
    user.login = login
    user.role = role
    user.role_id = role_id
    user.personal_number = personal_number
    user.residency = residency
    user.phone = phone

    try:
        db.session.commit()
    except Exception as ex:
        print("DB exeption in User")
        print(ex)


@user_bp.route('/<int:id>/delete', methods=['GET'])
def remove_user(id):
    user = User.query.get(id)
    if not user:
        flash("No such user")
        return redirect("/home")
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect("/home")
    except Exception as ex:
        print(ex)
        flash("Program occurred an error while deleting user " + user.name)
        return redirect("/home")


@user_bp.route("/<int:id>/profile", methods=['GET','POST'])
def user_profile(id):
    user = User.query.get(id)
    if not user:
        flash("No such user")
        return redirect("/home")
      
    return render_template("user/user_profile.html", user=user)


@user_bp.route("/<int:id>/password_change", methods=['GET','POST'])
def password_change(id):
    user = User.query.get(id)
    if not user:
        flash("No such user")
        return redirect("/home")

    form = PasswordChangeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if bcrypt.check_password_hash(user.password, form.old_password.data):
                change_user_password(form=form, user=user)
            else:
                flash('Old password is incorrect', "warning")
        else:
            flash('Form is invalid', "warning")

    return render_template("user/password_change.html", form=form, user=user)


def change_user_password(form, user: User):
    user.password =  bcrypt.generate_password_hash(form.new_password.data).decode("UTF-8")
    db.session.commit()
    flash('Password has been changed', "warning")