from flask import Blueprint, jsonify, request
from flask_mail import Message
from app import db, mail

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/profile", methods=["PUT"])
def update_profile():
    data = request.json
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    user.name = data.get("name", user.name)
    user.title = data.get("title", user.title)
    user.phone = data.get("phone", user.phone)
    user.department = data.get("department", user.department)

    db.session.commit()
    return jsonify({
        "message": "Profile updated successfully",
        "user": {
            "name": user.name,
            "title": user.title,
            "phone": user.phone,
            "department": user.department
        }
    })

@api_bp.route("/send-test-email", methods=["GET"])
def send_test_email():
    msg = Message(
        subject="Test Email from Rwaq System",
        recipients=["asala.alsaaf@rwaqeng.com"],
        body="This is a test email sent from the deployed app on Render.com."
    )
    mail.send(msg)
    return jsonify({"message": "Test email sent successfully"})