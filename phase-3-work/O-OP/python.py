class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def smell(self):
        print("It reaks")
    def fall(self):
        self.hasFallen = False
        print("They can fall")

    @property
    def price(self):
        return self._price
    
    @price.setter   
    def price(self,price):
        if (isinstance(price,(int,float)) and price > 0):
            self._price = price
        else:
            print("Invalid price")  

prod1 = Product("flour", 189)             

class Goods(Product):
    def buy(self):
        print("I'ma but this toy")
    def steal(self):
        print("They stole a bicycle")
    def smell(self):
        super().smell()

good1 = Goods("wheat",200)
good2 = Goods("bicycle",30000)

good1.fall()
good2.steal()

print(good1.name,good2.price)