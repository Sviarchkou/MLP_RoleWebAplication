from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class UserCreationFrom(FlaskForm):
    username = StringField("ФИО", validators=[DataRequired(),Length(min=3, max=100)])
    password = PasswordField("Пароль",validators=[DataRequired()])
    confirm_password = PasswordField("Подтвердите пароль", validators=[DataRequired(), EqualTo('password')])
    personal_number = StringField("Номер в списке",validators=[Length(min=3, max=15)])
    residency = StringField("Место жительства", validators=[Length(min=3, max=50)])
    phone = StringField("Номер телефона", validators=[Length(min=3, max=15)])
