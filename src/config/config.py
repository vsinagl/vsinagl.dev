from flask import Flask
from os import getenv

def app_config(app: Flask):
    app.secret_key = getenv("VSINAGL_SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #we are not tracking all modifications to database
    app.config['MAIL_SERVER'] = getenv("MAIL_SERVER")
    app.config['MAIL_PORT'] = getenv("MAIL_PORT")
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")
    app.config['MAIL_DEFAULT_SENDER'] = getenv("MAIL_DEFAULT_SENDER")






