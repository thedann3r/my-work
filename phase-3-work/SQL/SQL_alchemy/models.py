#  define our table using sqlalchemy and OOP
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Text, Integer, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# connect to the db using sessionmaker (similar to sqlite conn)
engine = create_engine('sqlite:///app.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)

db = Session()

# create  a base model that all our models are going to inherit from
Base = declarative_base()

# define model
class User(Base):
    __tablename__ = "users"

# define columns
    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    email = Column(VARCHAR(), nullable=False, unique=True)#unique means 2 or more ids cant share the same email.
    cell_no = Column(VARCHAR(), nullable=True)

    # one-to-many
    accounts = relationship("Accounts", backref="users")

    def __repr__(self):
        return(f"users {self.id}, Name: {self.name}, Email: {self.email}, Number: {self.cell_no}")
    
class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer(), primary_key=True)
    working_balance = Column(Integer())
    balance = Column(Integer())
    credit_score = Column(Integer())
    user_id = Column(Integer(), ForeignKey('user.id'))

    # mant-to-one
    users = relationship("User", backref="accounts", uselist=False)

    # time stamp
    created_at = Column(DateTime(), default = datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
