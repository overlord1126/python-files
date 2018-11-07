from flask_login import login_required,logout_user
from flask_restful import Resource

class Logout(Resource):
    @login_required
    def get(self):
        logout_user()
        return "logout successfully"