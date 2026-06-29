class Employee:
    a = 1

    @classmethod  # instance attribute nai batave ee class attribute j batavse
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

# implemantation details are encapsulated user ne aa badhu khabar na pade e khali name lakhi ne jato re pan background ma ena name ne be rite levama ave chhe frist and last name em
# abstarction matlab implementation details chupavi didhi user jode thi.
# encapsulation no matlab bau badha kam karva vala components ne ek j unit ma pack kari didha jem aa case ma class chhe class Employee().
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

         
e = Employee()
e.a = 12 #Bhale tame ahiya amnual value nakho pan classmethod value change ni thava de bcoz of classmethod

e.name = "Ruchin patel"
print(e.name)

e.show()
