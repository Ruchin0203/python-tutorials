st = "Ruchin is a student"
f = open("myfile.txt", "w") # for write 
f = open("myfile.txt", "a") # add at end of file(append)
f.write(st)
f.close()