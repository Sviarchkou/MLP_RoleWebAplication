from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PasswordChangeForm(FlaskForm):
    old_password = PasswordField("Старый пароль",validators=[DataRequired()])
    new_password = PasswordField("Новый пароль",validators=[DataRequired()])
    confirm_password = PasswordField("Подтвердите пароль", validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField("Изменить пароль")