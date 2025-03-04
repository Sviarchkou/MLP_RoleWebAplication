from flask import Blueprint, render_template
# from flask_login import login_required

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/home')
@main_bp.route('/')
def index():
    return render_template("home_page.html")