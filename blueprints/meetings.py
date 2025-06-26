from flask import Blueprint

meetings_bp = Blueprint('meetings', __name__)

@meetings_bp.route('/meetings')
def meetings_home():
    return "صفحة الاجتماعات (قيد التطوير)"