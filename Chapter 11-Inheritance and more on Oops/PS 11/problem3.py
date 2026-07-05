class Employee:
    salary = 250
    increment = 20

    @property
    def salaryAfterIncerment(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncerment.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
print(e.salaryAfterIncerment)
e.salaryAfterIncrement = 300
print(e.increment)