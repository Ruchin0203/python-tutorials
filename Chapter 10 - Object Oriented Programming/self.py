class Employee:
    language = "py" #This is a class attribute
    salary = 120000

    def getInfo(self): #tamare ahiya self no use karvo j pade 
        print(f"The language is {self.language}.The salary is {self.salary}")
 
    # def greet(self):
    #     print(f"Good morning")
    
    @staticmethod # jo tame object attribute ne function ma na use karta hov to staticmethod use karvu.matlab name, language, salary thi tamne kai j fer na pade bas khali as a decorator use karvu.
    def greet():
        print(f"Good morning")
        
Ruchin = Employee()
Ruchin.language = "Java script" #This is an Instance(object) attribute
print(Ruchin.language, Ruchin.salary)
Ruchin.greet()
Ruchin.getInfo()
# Employee.getInfo(Ruchin) # uper vali line no matlab