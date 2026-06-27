class Employee: #parent class
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

# class Programmer:
#     company = "ITC InfoTech"
#     def show(self):
#         print(f"The name of employee is {self.name} and the company is {self.company}")

#     def showlanguage(self):
#         print(f"The name of employee is {self.name} and he is good with {self.language} language")


#code ne nano rakhava mate ane parent class update kari etle child(Derived) class update thai j jay
# Simply inheritance kari didhu. matlab employee ma jetla object hoy e badha programmer ma avi jay.ane jo pachal thi koi ferfar karvano thay to kahli employee ma j karvano etle child class ma automatic update (change) thai j jay  

class Programmer(Employee):# child(Derived) class
    company = "ITC Infotech"
    language = "Python"
    def showlanguage(self): 
        print(f"The name of employee is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company)
b.showlanguage()