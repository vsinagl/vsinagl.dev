from dataclasses import dataclass


@dataclass
class Message:
	name: str = ""
	email: str = ""
	message: str = ""
	ip_: str = ""
	date: str = ""

	def __repr__(self):
		return f"Message('{self.name}', '{self.email}', '{self.message}', '{self.ip_address}', '{self.date}')"