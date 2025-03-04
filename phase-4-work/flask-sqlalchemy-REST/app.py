from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from resources.rivers import RiverListResource, RiverResource
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rivers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

api = Api(app)

CORS(app)

api.add_resource(RiverListResource, '/rivers')
api.add_resource(RiverResource, '/rivers/<int:id>')

@app.route('/')
def home():
    return '<h1>Welcome to the rivers page!</h1>'

if __name__ == '__main__':
    app.run(debug= True)