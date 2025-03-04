from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
import os
# from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use Gmail SMTP server or your choice
# app.config['MAIL_PORT'] = 465  # Use port 465 for SSL or 587 for TLS
# app.config['MAIL_USE_SSL'] = True  # Use SSL connection for security
# app.config['MAIL_USE_TLS'] = False  # If you use SSL, set this to False
# app.config['MAIL_USERNAME'] = 'thedannoir@gmail.com'  # Your email (Gmail or other)
# app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your email password or app password
# app.config['MAIL_DEFAULT_SENDER'] = 'thedannoir@gmail.com'  # The "From" email address


# mail = Mail(app)

db = SQLAlchemy(app)
migration = Migrate(app, db)
CORS(app, supports_credentials=True)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
api = Api(app)

@app.route('/')
def index():
    return 'Welcome to the home page!'

class Users(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    # email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    role = db.Column(db.String, nullable = False, default = 'user')

    
class Products(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        # email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'user')

        # if "@gmail.com" not in email:
        #     return {'error' : 'Wrong email formating. Email must contain the "@gmail.com" symbol!'}, 401

        if Users.query.filter_by(username = username).first():
            return {'error' : 'Username or email already exists!'}, 400
        hash = bcrypt.generate_password_hash(password).decode('utf-8')
        newUser = Users(username = username, password = hash, role = role)

        db.session.add(newUser)
        db.session.commit()
        return {'message' : 'user created successfully!'}, 201
    
        # confirmation_msg = Message(
        #         subject="Welcome to Our Platform!",
        #         recipients=[email],
        #         body=f"Hi {username},\n\nThank you for signing up. We're excited to have you with us.\n\nBest,\nThe Team"
        #     )

        # mail_status = mail.send(confirmation_msg)

        # if mail_status is None:
        #     return {'message': 'User created successfully! A confirmation email has been sent.'}, 201
        # else:
        #     return {'error': 'Error sending confirmation email. Please try again later.'}, 500

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        # email = data.get('email')
        password = data.get('password')

        user = Users.query.filter_by(username = username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            create_token = create_access_token(identity={'username': user.username, 'role':user.role})
            refresh_token = create_refresh_token(identity={'username': user.username, 'role':user.role})
            return {'access_token':create_token, 'refresh_token':refresh_token, 'role':user.role}
        return {'error' : 'Username or password is incorrect!'}, 401
    
class DeleteAcc(Resource):
    @jwt_required()
    def delete(self):
        current = get_jwt_identity()
        current_user = Users.query.get(current)
        if not current_user:
            return {'error' : 'user not found!'}, 404
        db.session.delete(current_user)
        db.session.commit()
        return {'message' : 'user account deleted successfully!'}, 200

class Refresh(Resource):
    @jwt_required(refresh = True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_refresh_token(identity = current_user)
        return {'access_token':new_access_token}, 201

class Product(Resource):
    @jwt_required()
    def get(self):
        products = Products.query.all()
        return [{'id' : prod.id, 'name': prod.name} for prod in products]

class User(Resource):
    @jwt_required()   
    def get(self):
        current_user = get_jwt_identity()
        if current_user['role'] != 'admin':
            return {'error' : 'The user is forbidden!'}, 403
        user = Users.query.all()
        return [{'id':use.id, 'username':use.username, 'role':use.role} for use in user]
    
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(DeleteAcc, '/delete')
api.add_resource(Refresh, '/refresh')
api.add_resource(Product, '/products')
api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run(debug = True)