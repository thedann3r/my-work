from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

                                   # one  to  one relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    profile = db.relationship('Profile', back_populates = 'user', uselist = False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bio = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique = True)
    user = db.relationship('User', back_populates = 'profile' )
    
                                     #one to many relationship

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    students = db.relationship('Students', back_populates = 'teacher')

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), unique = True)
    teacher = db.relationship('Teacher', back_populates = 'students')

                                        # many to many relationship between learners and courses

enrollment = db.Table(
    'enrollment',
    db.Column('learners_id', db.Integer, db.ForeignKey('learners.id'), primary_key = True),
    db.Column('courses_id', db.Integer, db.ForeignKey('courses.id'), primary_key = True)
)    

class Learners(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    courses = db.relationship('Courses', secondary = enrollment, back_populates = 'learners')

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    learners = db.relationship('Learners', secondary = enrollment, back_populates = 'courses')