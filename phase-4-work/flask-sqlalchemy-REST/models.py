from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class River(db.Model, SerializerMixin):
    __tablename__ = "Rivers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    source = db.Column(db.String, nullable = False)
    length_in_km = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"<River Name: {self.name} Source: {self.source} Length: {self.length_in_km}>"