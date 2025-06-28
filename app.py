
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize extensions (moved to extensions.py)
db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///default.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")

    # Suppress emails if credentials are missing
    if not app.config["MAIL_USERNAME"] or not app.config["MAIL_PASSWORD"]:
        app.config["MAIL_SUPPRESS_SEND"] = True

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from blueprints.api import api_bp
    app.register_blueprint(api_bp)

    return app

# Entry point for Render or local running
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
