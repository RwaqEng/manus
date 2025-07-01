from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from extensions import db
from flask_migrate import Migrate
from users import User  # ✅ تم تصحيح المسار هنا

from dashboard import dashboard_bp
from tasks import tasks_bp
from meetings import meetings_bp
from api import api_bp
from auth import auth_bp

def create_app():
    app = Flask(__name__, static_url_path="/static")
    CORS(app)

    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(meetings_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
