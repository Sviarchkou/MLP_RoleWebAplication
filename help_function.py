from models.user import User, current_user


def check_user_permission(id, login):
    try:
        user = User.query.filter_by(login=login).first()
        if id != user.id:
            return False
        return user
    except:
        return False


def check_if_admin(login):
    try:
        user = User.query.filter_by(login=login).first()
        if not user:
            return False
        return user.role.isAdmin, user
    except:
        return False
