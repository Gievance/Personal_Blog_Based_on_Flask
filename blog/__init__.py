import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from blog.utils.seed import seed_demo_data


def create_app():
    if not os.path.exists("./blog/logs"):
        os.makedirs("./blog/logs")

    handler = RotatingFileHandler(
        "./blog/logs/blog.log",
        encoding="utf-8",
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )


    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = app.config.get("SECRET_KEY") or os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    db.init_app(app)

    from blog.home import home

    app.register_blueprint(home)

    with app.app_context():
        db.create_all()
        # seed_demo_data()
    app.logger.info("开启WNBlog项目！")
    return app


def create_debug_app():
    return create_app()
