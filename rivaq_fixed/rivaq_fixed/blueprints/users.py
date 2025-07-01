from flask import Blueprint

# تصحيح مسار الاستيراد لنموذج User
from rivaq_fixed.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def users_home():
    return "صفحة المستخدمين (قيد التطوير)"

