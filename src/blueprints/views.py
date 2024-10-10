from flask import Blueprint, jsonify, render_template, request, url_for, redirect, session, flash
from os import getenv
from dotenv import load_dotenv
import yaml
from datetime import datetime


views = Blueprint("views", "home")

@views.route("/")
def home():
    args = request.args
    username = args.get('name')
    with open('projects.yaml') as file:
        data = yaml.safe_load(file)
    return render_template("index.html", name = username, projects=data, now=datetime.now().strftime('%Y'))

@views.route("/aboutme")
def about():
    return "<h1> work in progress </h1>"


@views.route("/json")
def get_json():
    return jsonify({'name':'Viktor', 'age': 25})

@views.route("/redirect")
def redirect_about():
    return redirect(url_for("views.aboutme"))


@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['username']
        user = request.form['password']
    else:
        return render_template("login.html")


