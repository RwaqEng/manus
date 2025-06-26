<<<<<<< HEAD
from flask import Blueprint, jsonify, request
from flask_mail import Message
from app import db, mail
from models import User

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/profile", methods=["PUT"])
def update_profile():
    data = request.form
    email = data.get("email")
    if not email:
        return jsonify({"success": False, "message": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    user.name = data.get("name", user.name)
    user.title = data.get("position", user.title)
    user.phone = data.get("phone", user.phone)
    user.department = data.get("department", user.department)
    user.join_date = data.get("join_date", user.join_date)
    user.manager_id = data.get("manager_id", user.manager_id)

    db.session.commit()
    return jsonify({"success": True, "message": "تم حفظ التعديلات بنجاح."})
=======
from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def api_index():
    return "Welcome to the Riwaq System API"
>>>>>>> dfdb57e4b0dd1eb7e289dca880e60daeea19843b
