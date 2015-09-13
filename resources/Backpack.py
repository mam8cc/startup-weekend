from flask import request
from flask.ext.restful import Resource, marshal_with, reqparse
from flask.ext.restful_swagger import swagger
from models.models import Backpack as BackpackModel, BackpackColorXref
from models.models import BackpackSize


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('torso', type=str, help='torso dimensions are required', required=True)
parser.add_argument('waist', type=str, help='waist dimensions are required', required=True)
parser.add_argument('gender', type=str, help='gender is required', required=True)
parser.add_argument('start', type=int, help='start date is required', required=True)
parser.add_argument('end', type=int, help='end date is required', required=True)


class Backpack(Resource):
    @swagger.operation(
        notes='This will recommend the best backpack based on requirements.  The following query params are REQUIRED:  torso, waist, gender, start(miliseconds), end(miliseconds)',
        responseClass=BackpackModel,
        nickname='recommend',
        responseMessages=[
            {
                "code": 201,
                "message": "Created. The URL of the created blueprint should be in the Location header"
            },
            {
                "code": 400,
                "message": "Required fields are missing."
            }
        ]
    )
    @marshal_with(BackpackModel.resource_fields, envelope='backpacks')
    def get(self):
        parser.parse_args()
        torso_dimension = request.args.get('torso', '')
        waist_dimension = request.args.get('waist', '')
        gender = request.args.get('gender', '')
        start_date = request.args.get('start', '')
        end_date = request.args.get('end', '')

        models = BackpackSize.query \
            .filter(BackpackSize.torso_range_low < torso_dimension) \
            .filter(BackpackSize.torso_range_high > torso_dimension) \
            .filter(BackpackSize.waist_range_low < waist_dimension) \
            .filter(BackpackSize.waist_range_high > waist_dimension) \
            .all()

        backpacks = []

        for backpackSize in models:
            if backpackSize.backpack.gender.name == gender or backpackSize.backpack.gender.name == "Unisex" :
                backpacks.append(backpackSize.backpack)

        for backpack in backpacks:
            backpack.colors = BackpackColorXref.query\
                .filter(BackpackColorXref.backpack_id==backpack.id).all()

        return backpacks


    def post(self):
        request_data = request.get_json()


