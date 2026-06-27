class Employee:
    a = 1

    @classmethod  # instance attribute nai batave ee class attribute j batavse
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 12 #Bhale tame ahiya amnual value nakho pan classmethod value change ni thava de bcoz of classmethod

e.show()
