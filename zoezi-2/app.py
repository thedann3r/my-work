from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

@app.route('/')
def home():
    return '<h1>Welcome to our books homepage!</h1>'

trade = db.Table(
    'trade',
    db.Column('books_id',db.Integer,db.ForeignKey('books.id'), primary_key = True),
    db.Column('buyer_id', db.Integer, db.ForeignKey('buyers.id'), primary_key=True)
)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(30))
    category = db.Column(db.String(20))
    buyers = db.relationship('Buyer', secondary = trade, back_populates = 'book')

class Buyer(db.Model):
    __tablename__ = "buyers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    book = db.relationship('Book', secondary = trade, back_populates = 'buyers')

    

if __name__ == '__main__':
    app.run(debug = True)
