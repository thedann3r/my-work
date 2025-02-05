from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_restful import Api,Resource
import os
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'

CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app) 
Session(app)
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.Integer, nullable = False)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if len(username) < 7 or len(username) > 20:
            return {'error': 'Username must contain between 7 and 20 characters!'}, 400
        if not re.search(r'[a-Za-z]', username):
            return {'error' : 'Username must contain at least 1 letter!'}, 400
        if not re.search(r'[0-9]', username):
            return {'error' : 'Username must contain atleast 1 number!'}, 400

        if User.query.filter_by(username=username).first():
            return {'error' : 'Username already exists!'}, 400
        hash = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hash)
        db.session.add(new_user)
        db.session.commit()
        return {'message' : 'User created successfully!'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return {'message' : 'User logged in successfully!'}, 200
        return {'error' : 'Invalid username or password! Please try again'},401
    
class IsLoggedIn(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return {'username' : user.username}, 200
        return {'error' : 'The user is not yet logged in!'}, 401

class Logout(Resource):
    def post(self):
        session.pop('user_id', None)
        return {'message' : 'User logged out successfully'}, 200
    
class DeleteUser(Resource):
    def delete(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'error' : 'The user is not yet logged in!'},401
        user = User.query.get(user_id)
        if not user:
            return {'error' : 'User not found!'}, 404
        db.session.delete(user)
        db.session.commit()
        session.pop("user_id", None)
        return {'message' : 'User deleted successfully!'},200


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(IsLoggedIn, '/loggedin')
api.add_resource(Logout, '/logout')
api.add_resource(DeleteUser, '/deleteuser')

if __name__ == '__main__':
    app.run(debug=True)