from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models.role import Role
from models.user import User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/home')
@main_bp.route('/')
@jwt_required()
def index():
    current_user = User.query.filter_by(login=get_jwt_identity()).join(Role).first()
    users = db.session.query(User).join(Role).order_by(User.personal_number).all()
    return render_template("home_page.html", users=users, current_user=current_user)
