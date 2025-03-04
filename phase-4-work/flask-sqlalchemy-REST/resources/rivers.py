from flask_restful import Resource
from flask import request
from models import River, db
    
class RiverListResource(Resource):
    def get(self):
        rivers = River.query.all()
        return [river.to_dict() for river in rivers]

    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in('name', 'source', 'length_in_km')):
            return {'error' : 'missing required fields!'}, 400
        new_river = River(
            name=data['name'],
            source=data['source'],
            length_in_km=data['length_in_km']
        )
        db.session.add(new_river)
        db.session.commit()
        return new_river.to_dict(),201

class RiverResource(Resource):
    def get(self, id):
        river = River.query.filter_by(id=id).first()
        if not river:
            return {'error' : 'river not found!'}, 404
        return river.to_dict(), 200

    def patch(self, id):
        data = request.get_json()
        river = River.query.get(id)

        if not river:
            return {"error" : "River does not exist!"}, 404
        if 'name' in data:
            river.name = data['name']
        if 'source' in data:
            river.source = data['source']
        if 'length_in_km' in data:
            river.length_in_km = data['length_in_km']
        db.session.commit()
        return river.to_dict(), 200

    def delete(self, id):
        river = River.query.get(id)
        if not river:
            return {"error" : "River does not exist!"}, 404
        db.session.delete(river)
        db.session.commit()
        return {"Message" : "River deleted successfully!"}, 200

