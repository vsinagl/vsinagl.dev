from flask import Blueprint, flash, render_template, request
from datetime import datetime
from config import limiter
from utils import Message, mailer
import re
from database import db, Messages

user = Blueprint("user", "user")

def validate_user_input(data: Message):
	"""
		function that validate user input
		return: tuple (Boolean, String), where String is error message
	"""
	email = data.email
	# regular expression pattern:
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	if not re.match(pattern, email):
		return (False, "Invalid email")
	if len(data.message) > 1000 or len(data.message) < 5:
		return (False, "Message must be between 5 1000 characters")
	return (True, None)

def check_empty_fields(data: Message):
	"""
		function that check if there are empty fields
		return: Boolean
	"""
	if data.email == "" or data.name == "" or data.message == "":
		return True
	return False


@user.route("/contact", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def contact():
	contact = Message()
	if request.method == "POST":
		contact.name = request.form['name']
		contact.email = request.form['email']
		contact.message = request.form['message']
		contact.ip_address = request.remote_addr
		contact.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		if check_empty_fields(contact):
				flash("Please fill all the fields")
				return render_template("contact.html")
		validation = validate_user_input(contact)
		if not validation[0]:
			flash(f"{validation[1]}")
			return render_template("contact.html")
		db_record = Messages(contact)
		db.session.add(db_record)
		db.session.commit()
		succes, message = mailer.sendme_contact(contact)
		if not succes:
			flash(f"Error on server side at sending email: {message}")
			return render_template("contact.html")
		flash ("Your message was sucesfully sent ")
		return render_template("contact.html")
	else:
		return render_template("contact.html")
		





