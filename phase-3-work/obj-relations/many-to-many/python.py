class Comrades:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def enroll(self,course):
        if not isinstance (course,Course):
            raise TypeError("Must be an instance of Course class")
        self.courses.append(course)
        course.comrades.append(self)

    def no_of_studs(self):
        return len(self.courses)

com1 = Comrades("Dann")
com2 = Comrades("Emmanuel")
com3 = Comrades("Mitchele")
com4 = Comrades("Alyce")

class Course:
    def __init__(self,name):
        self.name = name
        self.comrades = []

    def no_of_courses(self):
        return len(self.comrades)

math = Course("Mathematics")
geo = Course("Geography")

com1.enroll(math)
com2.enroll(geo)
com2.enroll(math)
com3.enroll(geo)
com4.enroll(math)
com4.enroll(geo)

print(f"{com4.name} takes the following {com4.no_of_studs()} courses:")
for com in com4.courses:
    print(f"{com.name}")

print(f"{geo.name} is being taken by the following {geo.no_of_courses()} students:")
for sub in geo.comrades:
    print(f"{sub.name}")




