import random
"""
s(1) for snake 
w(-1) for water 
g(0) for gun
"""
computer = random.choice([-1, 0, 1])
youstr = input("Entre your choice: ")
youDict = {"s": 1,"w": -1, "g": 0}
reverseDict = { 1: "Snake", -1: "Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(you == computer):
    print("it's a draw!")

else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You loos!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==1 and you==-1):
        print("You loos!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==0 and you==1):
        print("You loos!")
    else:
        print("something went wrong!")
    # if((computer - you) == -1 or (computer - you) == 2):
    #     print("You loos!")
    # else:
    #     print("You win!") 
        
    # this shortcut made by logocally
