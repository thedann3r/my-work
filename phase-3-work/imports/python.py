from functions.addition import add
from functions.addition import Human
from functions.product import prod

from functions.helpers.combined import combined

print(add(11,11))
print(prod(12,12))

print(combined(11,11,12,12))

class Student(Human):
        pass

stud = Student()

stud.run()
stud.walk()