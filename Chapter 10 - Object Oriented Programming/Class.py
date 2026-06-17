class Employee:
    language = "py" #This is a class attribute
    salary = 120000

Ruchin = Employee()
Ruchin.name = "Ruchin" #This is an Instance(object) attribute
print(Ruchin.name, Ruchin.language, Ruchin.salary)

Alice = Employee()
Alice.name = "Alice"
print(Alice.name, Alice.language, Alice.salary)

#Here name is instance attribute and salary and language are  class attributes as they directly belong to the class