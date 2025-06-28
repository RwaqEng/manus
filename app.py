
import os
from flask import Flask
from dotenv import load_dotenv

from extensions import db, mail
from models import User

def create_app():
    # Load environment variables
    load_dotenv()

    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # Sample index route
    @app.route("/")
    def index():
        return "Hello from Riwaq!"

    # Register blueprints or add routes here if needed
    from api import api_bp
    app.register_blueprint(api_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
