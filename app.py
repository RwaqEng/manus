from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

# Initialize Flask extensions (instances only)
db = SQLAlchemy()
mail = Mail()
csrf = CSRFProtect()


def create_app(config_name: str | None = None) -> Flask:
    """Application factory for the Rivaq system.

    This adopts best-practice structure: one app per call, lazy configuration,
    and extension instances shared across blueprints. Routes have been
    migrated out to dedicated blueprints to keep this file small and
    maintainable.
    """
    # Load environment variables from .env early
    load_dotenv()

    # Resolve configuration object
    from config import config as config_map  # local import to avoid circular refs
    config_name = config_name or os.getenv("FLASK_ENV", "development")
    if config_name not in config_map:
        config_name = "default"

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_map[config_name])

    # --- Initialise extensions ---
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    # Guard e-mail sending when credentials are absent (local dev / CI)
    if not (app.config.get("MAIL_USERNAME") and app.config.get("MAIL_PASSWORD")):
        mail.suppress = True

    # Ensure upload directory exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # --- Register blueprints ---
    # Blueprints are defined in the blueprints/ package (to be created next)
    from blueprints.auth import auth_bp
    from blueprints.tasks import tasks_bp
    from blueprints.meetings import meetings_bp
    from blueprints.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(meetings_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    # Default route shortcut
    @app.route("/")
    def index():
        return "Rivaq Task Management System is running!"

    # Expose useful objects in `flask shell`
    @app.shell_context_processor
    def _make_shell_ctx():
        return {"db": db, "app": app}

    return app


# ---------------------------------------------------------------------------
# CLI helper: initialise / seed the database ---------------------------------
# ---------------------------------------------------------------------------

def _seed_db(app: Flask):
    """Invoke existing seed script within an app context."""
    from init_db import init_database

    with app.app_context():
        init_database()


if __name__ == "__main__":
    # Running directly e.g. `python app.py` → dev server
    flask_app = create_app()
    _seed_db(flask_app)  # create tables & sample data if DB empty
    flask_app.run(
        host="0.0.0.0",
        port=5000,
        debug=flask_app.config.get("DEBUG", False)
    )