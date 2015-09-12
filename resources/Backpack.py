from flask import request
from flask.ext.restful import Resource, marshal_with
from flask.ext.restful_swagger import swagger
from models.models import Backpack


class Backpack(Resource):

    @swagger.operation(
        notes='This will recommend the best backpack based on requirements.',
        responseClass=Backpack,
        nickname='recommend',
        responseMessages=[
            {
              "code": 201,
              "message": "Created. The URL of the created blueprint should be in the Location header"
            },
            {
              "code": 405,
              "message": "Invalid input"
            }
          ]
        )
    @marshal_with(Backpack.resource_fields)
    def get(self):
        torso_dimension = request.args.get('torso', '')
        waist_dimension = request.args.get('waist', '')
        gender = request.args.get('gender', '')
        start_date = request.args.get('start', '')
        end_date = request.args.get('end', '')



    def post(self):
        request_data = request.get_json()

