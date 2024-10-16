from flask import Flask
from blueprints import views, admin, user
from dotenv import load_dotenv
from config import limiter, recaptcha, app_config
from database import db
from utils import mailer
import os
from waitress import serve



def create_app():
    load_dotenv()
    app = Flask(__name__)
    app_config(app)

    # declaring flask extensions
    limiter.init_app(app)
    mailer.mail.init_app(app)
    #recaptcha.init_app(app)

    #setting up database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    #registering blueprints
    app.register_blueprint(views, url_prefix="/", name="views")
    app.register_blueprint(admin, url_prefix="/admin", name="admin")
    app.register_blueprint(user, url_prefix="/user", name="user")

    return app


if __name__ == "__main__":
    app = create_app()
    #app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)), debug=True)
    serve(app, host='0.0.0.0', port='8000')
