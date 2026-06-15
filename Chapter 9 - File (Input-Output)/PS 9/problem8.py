# 8. Write a program to make a copy of a text file “this. txt” 

with open("file.txt") as f:
    content = f.read()

with open("copy_file.txt", "w") as f:
    f.write(content)