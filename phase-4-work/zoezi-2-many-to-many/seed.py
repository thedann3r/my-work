from app import app,db, Book,Buyer,trade
from faker import Faker

fake = Faker()

with app.app_context():
    Book = []
    book1 = Book
    