from flask_restful import Resource,marshal_with,fields,abort
from model.UsersModel import UsersModel
from flask import request,jsonify

user_fields = {
	'id': fields.Integer,
    'name': fields.String,
	'password': fields.String,
	'type': fields.Integer,
	'shops': fields.String
}
class Users(Resource):
	@marshal_with( user_fields,envelope="data" )
	def get(self):
		return UsersModel.query.all()