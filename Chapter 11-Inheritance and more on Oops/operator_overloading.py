class Number:
    def __init__(self, n):
        self.n = n

#koi pan be operand uper shu operation thay  ane ene customize karvu hoy to aa prakar na methods ne overload kari shakie 

    def  __add__(self, num):
        return self.n + num.n


n = Number(2)
m = Number(3)

print(n+m)