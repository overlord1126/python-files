from flask import Flask 
from flask_restful import Api,Resource

from resources.login import login_manager

from resources.shops import Shops
from resources.menus import Menus
from resources.users import Users
from resources.login import Login
from resources.logout import Logout
from resources.register import Register

from db import db
app = Flask("app")
api = Api( app )


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/ele'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "66666"

db.init_app(app)
login_manager.init_app(app)

api.add_resource( Shops,"/shop" )
api.add_resource( Menus,"/menu" )
api.add_resource( Users,"/user" )
api.add_resource( Login,"/login" )
api.add_resource( Logout,"/logout" )
api.add_resource( Register,"/register" )

if __name__ == "__main__":
	app.config['JSON_AS_ASCII'] = False
	app.run( debug = True )