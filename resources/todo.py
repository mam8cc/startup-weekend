from flask.ext.restful import Resource
from flask.ext.restful_swagger import swagger


class ToDo(Resource):

    "Get a ToDo"
    @swagger.operation(
        notes='Get a ToDo',
        nickname='upload',
        responseMessages=[
            {
              "code": 200,
              "message": "Its all good bruh."
            }
          ]
        )
    def get(self):
        return 'Got a todo!'