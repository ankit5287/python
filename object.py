class car:
    def __init__(self,model,price):
        self.model = model
        self.price = price
    
bmw = car("m4","2cr")

print(bmw.model)
print(bmw.price)

#------------------------------------------------------------------------------------------------

# Accessing class object

class details:
    def __init__(self,model):
        self.model = model
    
    def setprice(self,price):
        self.price =price
        
    def getprice(self):
        return self.price
    
car = details("2026")
car.setprice("2cr")
print(f"car price:{car.getprice()}")

car2 = details("2023")
car2.setprice("1cr")
print(f"car2 price:{car2.getprice()}")
print(f"car model:{car2.model}")

# Deleting an object

del car
print(f"car price:{car.getprice()}")
