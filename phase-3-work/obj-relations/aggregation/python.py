class Engine:
    def __init__(self,engine_type):
        self.engine_type = engine_type

class Car:
    def __init__(self,name,make,engine):
        self.name = name
        self.make = make
        self.engine = engine

engine = Engine("v12")
car1 = Car("Pagani","Italian",engine)

print(car1.engine.engine_type)