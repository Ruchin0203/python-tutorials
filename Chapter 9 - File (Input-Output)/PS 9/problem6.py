# 6. Write a program to mine a log file and find out whether it contains ‘python’. 

with open("log.txt") as f:
    c = f.read()
    x = c.find("python")
    
    if("python" in c):
        print("python is present in log file.")
    else:
        print("python is not present in log file.")