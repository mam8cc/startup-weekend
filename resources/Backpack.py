from flask import request
from flask.ext.restful import Resource


class Backpack(Resource):

    def get(self):
        torso_dimension = request.args.get('torso', '')
        waist_dimension = request.args.get('waist', '')
        gender = request.args.get('gender', '')
        start_date = request.args.get('start', '')
        end_date = request.args.get('end', '')



    def post(self):
        request_data = request.get_json()

