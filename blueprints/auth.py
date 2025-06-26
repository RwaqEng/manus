<<<<<<< HEAD
from flask import Blueprint, render_template
=======
from flask import Blueprint
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
<<<<<<< HEAD
    return render_template("auth/login.html")
=======
    return "صفحة تسجيل الدخول (قيد التطوير)"
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b
