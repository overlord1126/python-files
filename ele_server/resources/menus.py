from model.MenusModel import MenusModel
from flask_restful import Resource,marshal_with,fields,abort
from flask import request
from flask_login import login_required

menus_fields = {
	"id": fields.Integer,
	"item_id" :fields.Integer,
	"name" : fields.String(),
	"restaurant_id" : fields.Integer(),
	"photos" : fields.String(),
	"rating" : fields.Float(),
	"satisfy_rate" : fields.Float(),
	"rating_count" : fields.Integer(),
	"satisfy_count" : fields.Integer(),
	"original_price" : fields.Float(),
	"price" : fields.Float(),
	"sold_out" : fields.Integer(),
	"month_sales" : fields.Integer()
}


class Menus ( Resource ):
	# @login_required
	@marshal_with( menus_fields,envelope="data" )
	def get( self ):
		restaurant_id = request.args.get( "restaurant_id" )
		if restaurant_id is None:
			# return {"msg": "参数中缺少 restaurant_id"},400
			abort( 404,message="restaurant_id is required" )
		else :
			menus = MenusModel.query.filter( MenusModel.restaurant_id == restaurant_id ).all()
			return menus
	@login_required
	def post( self ):
		restaurant_id = request.form.get("restaurant_id")
		name = request.form.get("name")
		if restaurant_id is None or\
			name is None:
			return {"msg":"缺少必要参数!"}
		elif 


