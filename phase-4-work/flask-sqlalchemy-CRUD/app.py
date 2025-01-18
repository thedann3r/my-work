from flask import Flask, jsonify, request
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

    #GET method

@app.route('/rivers', methods=['GET'])
def get_river():
    rivers = River.query.all()
    return jsonify([river.to_dict() for river in rivers])

@app.route('/rivers/<int:id>', methods=['GET'])
def get_one(id):
    river = River.query.get(id)
    if not river:
        return jsonify({"message" : "River does not exist!"}), 404
    return jsonify(river.to_dict()), 200

    #POST method

@app.route('/rivers', methods=['POST'])
def get_new():
    data = request.get_json()
    if not data or not all(key in data for key in ("name", "source", "length_in_km")):
        return jsonify({"error" : "missing required field(s)!"}), 400
    new_river = River(
        **data
        # name = data['name'],
        # source = data['source'],
        # length_in_km = data['length_in_km']
    )
    db.session.add(new_river)
    db.session.commit()
    return jsonify(new_river.to_dict()), 201

    #PATCH/PUT method

@app.route('/rivers/<int: id>', methods=['PUT','PATCH'])
def update_one(id):
    data = request.get_json()
    river = River.query.get(id)

    if not river:
        return jsonify({"error" : "River does not exist!"}), 404
    if 'name' in data:
        river.name = data['name']
    if 'source' in data:
        river.source = data['source']
    if 'length_in_km' in data:
        river.length_in_km = data['length_in_km']
    db.session.commit()
    return jsonify(river.to_dict()), 200

    #DELETE

@app.route('/rivers/<int:id>', methods=['DELETE'])
def delete_one(id):
    river = River.query.get(id)
    if not river:
        return jsonify({"error" : "River does not exist!"}), 404
    db.session.delete(river)
    db.session.commit()
    return jsonify({"Message" : "River deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug= True)