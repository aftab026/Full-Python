# snake water gun game or as like rock paper scissors

import random


def gameWin(comp, you):
    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    #Check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
             return True
                
    #Check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
             return True


comp = print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif random == 3:
    comp = 'g'

you = input("YOur Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Compute chose {comp}")
print(f"Your chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("you Win!")
else:
    print("you Lose!")
