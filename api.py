from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from flask_restful_swagger import swagger
from models.models import db
from resources.Backpack import Backpack as BackpackResource
from resources.colors import Colors as ColorResource
from resources.packages import Packages

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://roabsgdavgefbn:-nEpKZ4MYIgFr2nD4v-alYOxjt@ec2-107-21-105-116.compute-1.amazonaws.com:5432/d4p18lbmbjfe21'
db.init_app(app)
CORS(app, resources=r'/*', allow_headers='Content-Type')
api = swagger.docs(Api(app), apiVersion='0.1')
api.add_resource(BackpackResource, '/backpack')
api.add_resource(ColorResource, '/backpack/<int:backpack_id>/colors')
api.add_resource(Packages, '/packages', '/packages/<int:package_id>')

if __name__ == '__main__':
    app.run(debug=True)
