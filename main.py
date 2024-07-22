# (1 for rock) (-1 for paper) (0 for scissors)
import random

computer = random.choice([-1, 0, 1])
yourstr = input("Enter your choice: ")

yourDict = {"r" : 1, "p" : -1, "s" : 0}
reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

you = yourDict[yourstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw!")

else:
    if((you == 1) and (computer == 0)):           # rock  x scissor = rock 
        print("You Win!!")
        
    elif((you == 1) and (computer == -1)):        # rock  x paper = paper
        print("You Lost!!")
        
    elif((you == -1) and (computer == 1)):        # paper  x rock = paper
        print("You Win!!")
        
    elif((you == -1) and (computer == 0)):        # paper x scissor = scissor
        print("You Lost!!")
        
    elif((you == 0) and (computer == -1)):        # scissor x paper = scissor
        print("You Win!!")
        
    elif((you == 0) and (computer == 1)):         # scissor x rock = rock
        print("You Lost!!")
        
    else:
        print("Something went wrong")
    