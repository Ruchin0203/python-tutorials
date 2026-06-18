class Employee:
    language = "py" #This is a class attribute
    salary = 120000
    
    def __init__(self,name,salary,language): #dunder(duoble underscore) method which is automatically called
     self.name = name
     self.salary = salary
     self.language = language
     print("I am creating an object")     

Ruchin = Employee("Ruchin",10000,"Java script")
# Ruchin.language = "Java script" #This is an Instance(object) attribute
print( Ruchin.name, Ruchin.language, Ruchin.salary)