class twoDVectore:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vectore is {self.i}i + {self.j}j")
    
class ThreeDVectore(twoDVectore):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k    
        
    def show(self):
        print(f"The Vectore is {self.i}i + {self.j}j + {self.k}k")

a = twoDVectore(3, 4)
a.show()
b = ThreeDVectore(2, 1, 3)
b.show()