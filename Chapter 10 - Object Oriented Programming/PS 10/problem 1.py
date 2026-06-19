# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
      self.name = name
      self.salary = salary
      self.pin = pin

r = programmer("Ruchin", 120000, 386243)
print(r.name, r.salary, r.pin, r.company)
d = programmer("Dhruv", 120000, 386243)
print(d.name, d.salary, d.pin, d.company)