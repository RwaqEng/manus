<<<<<<< HEAD
from flask import Blueprint, render_template
=======
from flask import Blueprint
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b

meetings_bp = Blueprint('meetings', __name__)

@meetings_bp.route('/meetings')
<<<<<<< HEAD
def meetings():
    return render_template("meetings/list.html")
=======
def meetings_home():
    return "صفحة الاجتماعات (قيد التطوير)"
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b
