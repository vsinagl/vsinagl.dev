from flask import Flask
from views import views, admin
from dotenv import load_dotenv
from os import getenv



app = Flask(__name__)
app.secret_key = getenv("VSINAGL_SECRET_KEY")
app.register_blueprint(views, url_prefix="/", name="views")
app.register_blueprint(admin, url_prefix="/admin", name="admin")


# @app.route("/")
# def home():
#     return f'<h1 style="text-align: center;"> Nice man! </h1> {__name__}'


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=8000) #debug - when you change app file, it automaticaly reload the app script --> so you don't need to  reaload it again


