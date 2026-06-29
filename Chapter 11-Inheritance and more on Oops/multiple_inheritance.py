class Employee: #parent class
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

class coder: # parent class
    language ="python"
    def Printlanguage(self):
        print(f"Out of all language here is your language: {self.language}")


# ama uper an banne class ni method's ama avi jay

class Programmer(Employee,coder):# child(Derived) class 
    company = "ITC Infotech"
    # language = "JS"
    def showlanguage(self): 
        print(f"The name of employee is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company)
b.Printlanguage()