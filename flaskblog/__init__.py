from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


default_picture = "default.jpg"
static_path = Path("flaskblog/static")
instance_path = Path("instance")
instance_picture_path = instance_path.joinpath("profile_pics")


def create_app(config_class=Config) -> Flask:
    app = Flask(
        __name__,
        static_folder=static_path.stem,  # relative to script
        instance_path=instance_path.absolute(),
    )
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    with app.app_context() as _:
        # create db and tables if not exists
        db.create_all()

    # push the default picture from static to instance folder
    instance_picture_path.joinpath(default_picture).write_bytes(
        static_path.joinpath(default_picture).read_bytes()
    )

    return app
