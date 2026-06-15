# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

f = open("file.txt")
content = f.read()

if("Ruchin" in content):
    print("Ruchin is present in the file")
else:
    print("Ruchin is not present in the file")

f.close()