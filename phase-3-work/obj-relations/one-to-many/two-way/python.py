class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.tm = None

std1 = Students("Dann",19)
std2 = Students("Navajjah",23)
std3 = Students("Chris",22)

class Tm(Students):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.students = []

    def assign(self,student):
        self.students.append(student)
        student.tm = self

    def no_of_std(self):
        return len(self.students)

tm = Tm("Solomon",41)

tm.assign(std1)
tm.assign(std2)
tm.assign(std3)

# print(std2.tm.name)

print(f"{tm.name}, who is {tm.age} years old, has the following {tm.no_of_std()} students:")
for std in tm.students:
    print(f"-{std.name}; who is {std.age} years of age!")