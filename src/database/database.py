from flask_sqlalchemy import SQLAlchemy
from utils import Message

db = SQLAlchemy()

class Messages(db.Model):
	__id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	message = db.Column(db.String(1000), nullable=False)
	ip_address = db.Column(db.String(50), nullable=False)
	date = db.Column(db.String(50), nullable=False)

	def __init__(self, message: Message):
		self.name = message.name
		self.email = message.email
		self.message = message.message
		self.ip_address = message.ip_address
		self.date = message.date

	def __repr__(self):
		return f"Message('{self.name}', '{self.email}', '{self.message}', '{self.ip_address}', '{self.date}')"