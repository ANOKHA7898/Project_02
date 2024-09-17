#Python project for Rock paper scissor Game

import random

options = ["rock","paper","scissor"]

#option[0]=rock
#option[1]=paper
#option[2]=scissor


user_win = 0
system_win = 0
tie = 0

while True:
    user_input = input("Enter Rock/Paper/Scissor or Q to Quite :").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Please Enter Valid Option")
        continue

    random_num = random.randint(0,2)
    
    system_pick = options[random_num]
    
    print("Computer:",system_pick)

    if user_input == "paper" and system_pick == "rock":
        print("You Won !")
        user_win+=1
    elif user_input == "scissor" and system_pick == "paper":
        print("You Won !")
        user_win+=1
    elif user_input == "rock" and system_pick == "scissor":
        print("You Won !")
        user_win+=1
    elif user_input == system_pick:
        print("Game tie !")
        tie+=1
        
    else:
        print("You Lose !")
        system_win+=1

print("-"*20)
print("You Won :" , user_win,"times")
print("System Won :",system_win,"times")
print("Tie :",tie,"times")
print("GOOD BYE !")
print("-"*20)
