from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from flask_restful_swagger import swagger
from models.models import db
from resources.Backpack import Backpack as BackpackResource

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://eglwyuhzapnpqc:WCJteKjRmtakk5-_MHU4VRa-uj@ec2-54-204-43-139.compute-1.amazonaws.com:5432/d64ekjunetosea'
db.init_app(app)
CORS(app, resources=r'/*', allow_headers='Content-Type')
api = swagger.docs(Api(app), apiVersion='0.1')
api.add_resource(BackpackResource, '/backpack')

if __name__ == '__main__':
    app.run(debug=True)
