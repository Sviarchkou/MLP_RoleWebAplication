from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserEditFrom(FlaskForm):
    name = StringField("ФИО", validators=[DataRequired(),Length(min=3, max=50)])
    login = StringField("Логин", validators=[DataRequired(), Length(min=3, max=20)])
    role = StringField("Роль", validators=[DataRequired()])
    personal_number = StringField("Номер в списке",validators=[Length(min=3, max=15)])
    residency = StringField("Место жительства", validators=[Length(min=3, max=50)])
    phone = StringField("Номер телефона", validators=[Length(min=3, max=30)])
    submit = SubmitField("Изменить")