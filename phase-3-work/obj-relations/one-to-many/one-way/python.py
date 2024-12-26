class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

std1 = Students("Dann",19)
std2 = Students("Navajjah",23)
std3 = Students("Chris",21)

class Tm:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.students = []

    def assign(self,student):
        self.students.append(student)


tm = Tm("Solomon", 41)

tm.assign(std1)
tm.assign(std2)
tm.assign(std3)

print(f"{tm.name} has the following students:")
for stud in tm.students:
    print(f"-{stud.name}; who is {stud.age} years old!")

# print(std1.name)