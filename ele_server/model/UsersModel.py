from db import db
from flask_login import UserMixin

class UsersModel (UserMixin,db.Model):
	__tablename__ = "user"
	id = db.Column( db.Integer,primary_key=True )
	name = db.Column( db.String )
	password = db.Column( db.String )
	type = db.Column( db.Integer )
	shops = db.Column( db.String )