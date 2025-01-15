from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db =  SQLAlchemy(app)
migrate = Migrate(app,db)

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    teacher = db.Column(db.String(20),nullable=False)

@app.route('/')
def Home():
    return 'im home, again'

if __name__ == "__main__":
    app.run(debug = True)