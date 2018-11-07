from db import db;

class MenusModel(db.Model):
	__tablename__ = "menus"
	id = db.Column( db.Integer(), primary_key=True )
	item_id = db.Column( db.BigInteger() )
	name = db.Column( db.String( 100 ) )
	restaurant_id = db.Column( db.Integer() )
	photos = db.Column( db.String( 2000 ) )
	rating = db.Column( db.Float() )
	satisfy_rate = db.Column( db.Float() )
	rating_count = db.Column( db.Integer() )
	satisfy_count = db.Column( db.Integer() )
	original_price = db.Column( db.Float() )
	price = db.Column( db.Float() )
	sold_out = db.Column( db.Integer() )
	month_sales = db.Column( db.Integer() )
	