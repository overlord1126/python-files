from flask_restful import Resource
from flask import request,jsonify
from model.UsersModel import UsersModel
from db import db

class Register (Resource):
	def get(self):
		name = request.args.get("name");
		psw = request.args.get("psw");
		confirmpsw = request.args.get("confirmpsw");
		print( name,psw,confirmpsw )
		if name is None or psw is None or confirmpsw is None :
			return jsonify({"msg":"缺少必要参数!"})
		elif psw != confirmpsw :
			return jsonify({"msg":"两次密码输入不一致!"})
		user = UsersModel.query.filter( UsersModel.name == name ).first()
		if user is not None:
			return jsonify({"msg":"用户名已经存在!"})
		new_user = UsersModel(name=name,password=psw,type=0)
		db.session.add( new_user ) 
		db.session.commit()
		print( new_user )

		return jsonify({"msg":"注册成功!!"})