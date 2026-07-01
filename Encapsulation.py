# Encapsulation - Encapsulation is about hiding access (putting a lock on the data so other parts of the code can't mess it up).
# __ in privet method 
class empDetails:
    def __init__(self,name,sal,id):
        self.name = name
        self.__sal = sal
        self._id = id
    
    def show_sal(self):
        print(f"Salary is:{self.__sal}")

    def getSal(self):
        print(self.__sal)

    def setSal(self,amount):
        if amount>0:
            self.__sal = amount
        else:
            print("Sallary value is incorrect")

emp1 = empDetails("gaurav",90000,1)
print(emp1.name)
# print(emp1.__sal())
emp1.show_sal() #Access using indirect method

# _ in protected method - Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
#--------------------------------------------
class subClass(empDetails):
    def showid(self):
        print(self._id)
       

emp2 = subClass("Parv",100000,1)
emp2.showid()

#getter& setter method for accessing privet attribute
#--------------------------------------------

emp2.getSal()
emp2.setSal(25000)
emp2.getSal()