from flask import Flask, request
from flask_mail import Mail, Message
from .message import Message as MessageModel


class ContactMailTemplate:
    def __init__(self, message: MessageModel):
        self.template = {
            "from_name": message.name,
            "recipient" : "viktor.sinagl@gmail.com",
            "subject": "You have new message at vsinagl.dev",
            "recipient": "viktor.sinagl@gmail.com",
            "body": (
                f"You have a new message at vsinagl.dev from {message.name}!\n"
                f"Sender email: {message.email}\n"
                f"Message:\n"
                f"{message.message}"
            )
        }


class Mailer:
    def __init__(self):
        self.mail = Mail()

    def sendme_contact(self, message: MessageModel ):
        template = ContactMailTemplate(message)
        try:
            msg = Message(template.template["subject"], recipients=[template.template["recipient"]], body=template.template["body"])
            self.mail.send(msg)
        except Exception as e:
            # TODO: log error
            print(e)
            return False, e
        return True, None

mailer = Mailer()






