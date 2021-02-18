import random
def gamewin(computer,you):
    if computer==you:
        return None
    elif computer=="s":
        if you=="w":
            return False
        elif you=='g':
            return True 
    elif computer=="w":
        if you=="g":
            return False
        elif you=='s':
            return True
    elif computer=="w":
        if you=="g":
            return False
        elif you=='s':
            return True 
                                
print("computer turn:snake(s) water(w) gun(g)")
randno=random.randint(1,3)
# print(randno)
if randno==1:
   computer="s"
elif randno==2:
   computer="w"    
elif randno==3:
   computer="g"
you=input("your turn:snake(s) water(w) gun(g)")
print(f"computer turn:{computer}")
print(f"your turn:{you}")
a=gamewin(computer,you)
if a==None:
    print("Game tie!")
elif a:
    print("you win!")
else:
    print("you lose!")        