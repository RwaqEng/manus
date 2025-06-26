<<<<<<< HEAD
from flask import Blueprint, render_template
=======
from flask import Blueprint
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks')
<<<<<<< HEAD
def tasks():
    return render_template("tasks/list.html")
=======
def tasks_home():
    return "صفحة المهام (قيد التطوير)"
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b
