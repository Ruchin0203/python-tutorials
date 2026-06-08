# Dict method

marks = {
      "Ruchin" : 100,
      "Rohit" : 80,
      " Mohit" : 20,
      0:"Ruchin"
}
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Ruchin":99,"Raman":84}))
print(marks) 
print(marks.get("Ruchin")) # If doesn't exist print None.
print(marks["Ruchin"]) # If doesn't exist return an error.

# print(marks.pop("Ruchin"))
print(marks.popitem())
print(marks)
