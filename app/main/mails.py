from flask_mail import Mail, Message
from flask import current_app

mail=Mail()

def init_mail(app):
    mail.init_app(app)

def send_email(subject, recipients, body=""):
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)
