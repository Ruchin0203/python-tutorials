def GoodDay(name, ending="Thank you"):
    print("Good Day, "+ name )
    print(ending)
    return "Done"
a = GoodDay("Ruchin", "Thank you!!") #aama default argument nai lage karan k ama alag thi Thank you!! lakhyu chhe
print(a) 
GoodDay("Raman") #aama default argument lagi jase thank you vali 
GoodDay("Rohan")