# 6. Write a program to calculate the factorial of a given number using for loop. 

# 4! = 1 x 2 x 3 x 4

n = int(input("Enter a number:"))
product = 1
for i in range(1, n+1):
    product = product*i
   
print(f"the factorial of {n} is {product}")    