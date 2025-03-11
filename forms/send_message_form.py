from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class SendMessageForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired(),Length(min=3, max=100)])
    desc = TextAreaField("Содержание", validators=[DataRequired()])
    user = StringField("Номер получателя", validators=[DataRequired()])
    submit = SubmitField("Отправить")