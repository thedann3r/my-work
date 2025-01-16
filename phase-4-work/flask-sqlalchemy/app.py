from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db =  SQLAlchemy(app)
migrate = Migrate(app,db)

class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    teacher = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f'<Student name: {self.name} age: {self.age}>'

@app.route('/')
def Home():
    return 'im home, again and again'
@app.route('/students')
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

if __name__ == "__main__":
    app.run(debug = True)