from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity

from forms.send_message_form import SendMessageForm
from models.role import Role
from extensions import db, bcrypt
from models.user import User
from models.message import Message


message_bp = Blueprint('message_bp', __name__)


@message_bp.route("/<int:id>/messages")
@jwt_required()
def show_messages(id):
    current_user = User.query.filter_by(login=get_jwt_identity()).join(Role).first()
    if current_user.id != id:
        flash("Invalid operation!", "warning")
        return redirect(url_for("main_bp.index"))
    messages = Message.query.filter_by(user_id=id).all()
    messages.reverse()
    return render_template("message/main_message.html", messages=messages, current_user=current_user)


@message_bp.route("/<int:id>/send_message", methods=['GET','POST'])
@jwt_required()
def send_message(id):
    current_user = User.query.filter_by(login=get_jwt_identity()).join(Role).first()
    if current_user.id != id:
        flash("Invalid operation!", "warning")
        return redirect(url_for("message_bp.show_messages", id))

    form = SendMessageForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(personal_number=request.form['user']).first()
            if user:
                return send(current_user, user)
            else:
                flash("No user with such personal number")
        else:
            flash("Form is invalid")
    return render_template("message/send_message.html", form=form, current_user=current_user)


def send(current_user:User, user: User):
    desc = str(request.form['desc'])
    desc +=" * Отправитель: " + current_user.name + f" ({current_user.role.name}) *"
    user_id = user.id
    message = Message(title=request.form['title'],
                      desc=desc,
                      user_id=user_id)
    try:
        db.session.add(message)
        db.session.commit()
    except Exception as ex:
        print("DB exeption in User")
        print(ex)

    flash("Сообщение отправлено")
    return redirect(url_for("main_bp.index"))