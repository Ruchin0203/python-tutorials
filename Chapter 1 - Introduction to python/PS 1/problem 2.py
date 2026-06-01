# 2. Write a python program to print the contents of a directory using the os module. 

import os

# specify the directory you want to list
directory_path = '/usb drive'

# list all files and directories in the specified path 
contents = os.listdir(directory_path)

# print each file and directory name
# for item in contents:
#  print(item)
print(contents)
