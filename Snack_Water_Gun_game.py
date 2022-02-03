    #                                    Snack Water Gun game 
import random
                                    #   define function gameWin to selection  of winner
def gameWin(comp, you):
    if comp == you :
        return None

    elif comp =='s' :
        if you=='w' :
           return False
        elif you =='g' :
            return True
    
    elif comp =='w' :
        if you =='s':
            return True
        elif you =='g' :
            return False
    
    elif comp =='g' :
        if you=='s':
            return False 
        elif you =='w':
            return True
    
    #                    Get Random values for the computer turn By using Random module
print("Computer's Turn : Snake(s) Water(w) Gun(g) :")
randNo =random.randint(1,3)

if randNo ==1 : 
    comp ='s'
elif randNo==2 :
    comp ='w'
elif randNo ==3 :
    comp ='g'
                    #  Get input from the User
you= input("Your's Turn : Snake(s) Water(w) Gun(g) :")

print(f"Computer Choose : {comp}")
print(f"You Choose : {you}")

    #             print who is winner
a= gameWin(comp, you)
if a==None:
    print("Game is tie")
elif a:
    print("You win")
else :
    print("You loose")