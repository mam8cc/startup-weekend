from api import Backpack
from flask import request
from flask.ext.restful import Resource
from flask.ext.restful_swagger import swagger


class Backpack(Resource):

    "Describing elephants"
    @swagger.operation(
        notes='This will recommend the best backpack based on requirements.',
        responseClass=Backpack,
        nickname='recommend',
        parameters=[
            {
              "query_params": ["torso", "waist", "gender", "start", "end"],
            }
          ],
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
    def get(self):
        torso_dimension = request.args.get('torso', '')
        waist_dimension = request.args.get('waist', '')
        gender = request.args.get('gender', '')
        start_date = request.args.get('start', '')
        end_date = request.args.get('end', '')



    def post(self):
        request_data = request.get_json()

