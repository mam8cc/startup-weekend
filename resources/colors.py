from flask.ext.restful import Resource, marshal_with
from models.models import BackpackColorXref


class Colors(Resource):
    @marshal_with(BackpackColorXref.resource_fields)
    def get(self, backpack_id):
        colors = BackpackColorXref.query\
                    .filter(BackpackColorXref.backpack_id==backpack_id).all()

        return colors
