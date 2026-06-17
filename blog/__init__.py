import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from blog.utils.seed import seed_demo_data


def _is_vercel_environment():
    return os.getenv("VERCEL") == "1" or os.getenv("VERCEL_ENV") is not None


def _configure_logging(app):
    app.logger.setLevel(logging.INFO)

    if _is_vercel_environment():
        return

    log_dir = "./blog/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, "blog.log")
    has_same_handler = any(
        isinstance(handler, RotatingFileHandler) and getattr(handler, "baseFilename", "").endswith("blog.log")
        for handler in app.logger.handlers
    )
    if has_same_handler:
        return

    handler = RotatingFileHandler(
        log_path,
        encoding="utf-8",
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    app.logger.addHandler(handler)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = app.config.get("SECRET_KEY") or os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    _configure_logging(app)

    db.init_app(app)

    from blog.home import home

    app.register_blueprint(home)

    if not _is_vercel_environment():
        with app.app_context():
            db.create_all()
            # seed_demo_data()

    app.logger.info("开启WNBlog项目！")
    return app


def create_debug_app():
    return create_app()
