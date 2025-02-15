import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail, instance_picture_path
from flaskblog.models import User


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = instance_picture_path.joinpath(picture_fn)

    i = Image.open(form_picture)
    i.thumbnail(size=(125, 125))
    i.save(picture_path)

    return picture_fn


def send_reset_email(user: User):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request",
        sender="noreply@salt.ch",
        recipients=[user.email],
    )
    msg.body = f"""To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request then simply ignore this email and no changes will be made.
    """
    mail.send(msg)
