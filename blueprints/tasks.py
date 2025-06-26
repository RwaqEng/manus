from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks')
def tasks_home():
    return "صفحة المهام (قيد التطوير)"