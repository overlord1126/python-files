from flask_login import LoginManager,UserMixin,login_user

from flask_restful import Resource
from flask import request,jsonify
from model.UsersModel import UsersModel

login_manager = LoginManager()

@login_manager.user_loader
def load_user(userid):
    # print( userid )
    return UsersModel.query.get(userid)

@login_manager.unauthorized_handler
def unauthorized():
    return "please login(请登录)"

class Login (Resource):
	def get (self):
		name = request.args.get("name")
		psw = request.args.get("psw")
		res = {
            "msg": "用户登录成功"
        }
		if name is None or psw is None:
			res["msg"] = "缺少 用户名 或者 密码"
			return jsonify(res)
		else:
			user = UsersModel.query.filter( UsersModel.name == name ).first()
			if user is None:
				res["msg"] = "该用户名不存在!"
			elif user.password != psw:
				res["msg"] = "密码错误!!"
			else: 
				login_user( user )
		return jsonify(res)

		
