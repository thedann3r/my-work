from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rivers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)



class River(db.Model, SerializerMixin):
    __tablename__ = "Rivers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    source = db.Column(db.String, nullable = False)
    length_in_km = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"<River Name: {self.name} Source: {self.source} Length: {self.length_in_km}>"

@app.route('/')
def home():
    return '<h1>Welcome to the lengths of Rivers!</h1>'

@app.route('/rivers')
def get_river():
    rivers = River.query.all()
    return jsonify([rive.to_dict() for rive in rivers])

if __name__ == '__main__':
    app.run(debug= True)