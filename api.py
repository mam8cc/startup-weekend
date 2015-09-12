import os
from flask import Flask
from flask.ext.restful import  Api
from flask.ext.cors import CORS
from flask_restful_swagger import swagger
from resources.todo import ToDo

app = Flask(__name__, static_url_path='')
CORS(app)

api = swagger.docs(Api(app), apiVersion='0.1')

api.add_resource(ToDo, '/todo')


if __name__ == '__main__':
    app.run(debug=True)