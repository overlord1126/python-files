from db import db

class ShopsModel (db.Model):
	__tablename__ = "shop"
	id = db.Column( db.Integer(),primary_key=True )
	shop_id = db.Column( db.Integer() )
	name = db.Column( db.String() )
	shopLogo = db.Column( db.String() )