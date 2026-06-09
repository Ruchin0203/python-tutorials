marks1 = int(input("Enter your marks:"))
marks2 = int(input("Enter your marks:"))
marks3 = int(input("Enter your marks:"))

# check for total percentange
total_percentage=(marks1+marks2+marks3)/3

if(total_percentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
  print("You are passed",total_percentage)

else:
 print("You failed.Try again next year:",total_percentage)
