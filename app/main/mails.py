from flask_mail import Mail, Message
from flask import current_app

mail=Mail()

def init_mail(app):
    mail.init_app(app)

def send_email(subject, recipients, body=""):
    full_body = f"Subject: {subject}\n\n{body}"
    msg = Message("", recipients=recipients) 
    msg.body = full_body  
    print(f"Message Body: {msg.body}")

    mail.send(msg)
