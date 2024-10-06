from flask import Blueprint, jsonify, render_template, request, url_for, redirect, session, flash
from os import getenv
import os
from dotenv import load_dotenv
import yaml
from datetime import datetime


views = Blueprint(__name__, "home")
admin = Blueprint(__name__, "admin")

@views.route("/")
def profile():
    args = request.args
    username = args.get('name')
    with open('projects.yaml') as file:
        data = yaml.load(file)
    return render_template("profile.html", name = username, projects=data, now=datetime.now().strftime('%Y'))

@views.route("/aboutme")
def about():
    return "<h1> work in progress </h1>"


@views.route("/json")
def get_json():
    return jsonify({'name':'Viktor', 'age': 25})

@views.route("/redirect")
def redirect_about():
    return redirect(url_for("views.aboutme"))

@admin.route("/login",  methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        if user.lower() == getenv("ADMIN_USERNAME") and password == getenv("ADMIN_PASSWORD"):
            session['admin'] = user
            return redirect(url_for("admin.admin_page"))
        else:
            if user.lower() != getenv("ADMIN_USERNAME"):
                if user.lower() != getenv("ADMIN_PASSWORD"):
                    flash("You input wront username and password !")
                    return render_template("login.html")
                flash("You input wrong username !")
                return render_template("login.html")
            elif user.lower() != getenv("ADMIN_PASSWORD"):
                flash("You input wrong password !")
                return render_template("login.html")
    else:
        return render_template("login.html")

@admin.route("/logout")
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))

@admin.route("/")
def admin_page():
    if "admin" in session:
        user = session['admin']
        return (f"<h1> Welcome user: {user} </h1> lorem ipsum")
    else:
        return redirect(url_for("admin.login"))

