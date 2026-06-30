class Employee:
    a = 1

class programmer(Employee):
    b = 2

class Manager(programmer):
    c = 3 

o = Employee()
print(o.a) #Print the attribute 
# print(o.b) #show an error

o = programmer()
print(o.a,o.b)
# print(o.c)# show an error

o = Manager()
print(o.a,o.b,o.c)