from flask import Blueprint, render_template

from app.extensions import db
from app.models.user import User


test_bp = Blueprint('test_bp', __name__)


@test_bp.route('/user/<user>')
def index(name):
    user = User(username=name)
    db.session.add(user)
    db.session.commit()
    return render_template("home_page.html")