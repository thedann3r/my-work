from models import db, User
    #                                          CRUD methods

# 1. create

user = User(name= "Dann", email= "dann@gmail.com", cell_no= "0756892906")

# db.add(user)

# db.commit()

#2. read
# retrieve all records
users = db.query(User).all()
# print(users)

# retrieve a single record
user1 = db.query(User).filter(User.id == 3).first()
# print(user1)

# 3. update
# a. retrieve record
user2 = db.query(User).filter(User.id == 1).first()
# b. updte the necessary field
user2.cell_no = '0787654321'
user2.email = 'austindan168@gmail.com'
user2.name = 'Austin'
db.add(user2)
db.commit()

# 4. delete
# a. retrieve record
user3 = db.query(User).filter(User.id == 2).first()
# b. delete record
db.delete(user3)
db.commit()
