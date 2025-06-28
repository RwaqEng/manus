
from flask import Blueprint, jsonify, request
from flask_mail import Message
from extensions import db, mail  # ✅ تم التعديل هنا

api_bp = Blueprint("api", __name__)

@api_bp.route("/send-test-email")
def send_test_email():
    msg = Message(
        subject="Test Email",
        sender="asala.alsaaf@rwaqeng.com",
        recipients=["asala.alsaaf@rwaqeng.com"],
        body="This is a test email sent from Flask!"
    )
    mail.send(msg)
    return jsonify({"message": "Email sent successfully!"})
