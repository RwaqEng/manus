from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users_home():
    return "صفحة المستخدمين (قيد التطوير)"