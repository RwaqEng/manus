
from flask import Flask
from flask_mail import Mail
from blueprints.api import api_bp  # ✅ تمت إضافة هذا السطر

app = Flask(__name__)
mail = Mail()

# إعدادات الإيميل (تأكدي أنها صحيحة)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'asala.alsaaf@rwaqeng.com'
app.config['MAIL_PASSWORD'] = 'your_app_password_here'  # غيّريها لكلمة المرور الخاصة بك
app.config['MAIL_DEFAULT_SENDER'] = 'asala.alsaaf@rwaqeng.com'

mail.init_app(app)

# ✅ تسجيل البلوبرنت
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
