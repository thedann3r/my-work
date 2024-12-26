class Id:
    def __init__(self,id):
        self.id = id

class Parent:
    def __init__(self,name,home,id):
        if not isinstance (id,Id):
            raise TypeError ("Id number must be an instance of Id class")
        self.name = name
        self.home = home  
        self.id = id

id1 = Id(42574094)

try:
    danner = Parent("Austin","Siaya",id1)
except TypeError as e:
    print(e)    

print(f"{danner.name} goes to {danner.home} when schools close and {danner.id.id} is his adress")