from flask import Blueprint, render_template

meetings_bp = Blueprint('meetings', __name__)

@meetings_bp.route('/meetings')
def meetings():
    return render_template("meetings/list.html")
