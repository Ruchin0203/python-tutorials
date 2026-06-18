class Employee:
    language = "py" #This is a class attribute
    salary = 120000

Ruchin = Employee()
Ruchin.language = "Java script" #This is an Instance(object) attribute
print(Ruchin.language, Ruchin.salary)

#Instance attributes, take preference over class attributes during assignment & retrieval.