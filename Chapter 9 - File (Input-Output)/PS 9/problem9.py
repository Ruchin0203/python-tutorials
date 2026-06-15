# 9. Write a program to find out whether a file is identical & matches the content of another file. 
# 
with open("file.txt") as f:
    content1 = f.read()

with open("copy_file.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes this files are identical")

else:
    print("No this files are not identical")