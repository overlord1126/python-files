from flask_restful import Resource,marshal_with,fields,abort
from model.ShopsModel import ShopsModel
from flask import request,jsonify
from flask_login import login_required

shops_fields = {
    'id': fields.Integer,
    'shop_id': fields.Integer,
    'name': fields.String(100),
    'shopLogo': fields.String(200)
}
def abort_if_none(res):
    if res is None :
        abort( 404,message="does not exist" )

class Shops(Resource):
    @login_required
    @marshal_with( shops_fields,envelope="data" )
    def get(self):
        id = request.args.get("id")
        if id is not None: 
            shops = ShopsModel.query.filter( ShopsModel.shop_id == request.args.get("id") ).first()
        else :
            offset = request.args.get("offset") or 0
            limit = request.args.get("limit") or 10
            keyword = request.args.get("keyword")
            if keyword is None :
                shops = ShopsModel.query.offset( offset ).limit( limit ).all()
            else:
                shops = ShopsModel.query.filter( ShopsModel.name.ilike('%'+ keyword +'%') ).offset( offset ).limit( limit ).all()
        # shops = ShopsModel.query.paginate( 2,3,False ).items
        abort_if_none( shops )
        return jsonify(shops)