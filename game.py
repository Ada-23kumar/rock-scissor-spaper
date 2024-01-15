import random

def gameWin(comp, you):
    if comp == 'r':
        if you =='s':
            return True
        elif you == 'p':
            return False
    elif comp == 's':
        if you=='p':
            return False
        elif you == 'r':
            return True
    elif comp =='p':
        if you == 's':
            return True
        elif you == 'r':
            return False
print("comp Turn : rock(r), paper(p), scissor(s)? :")
comp = ' '
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 's'
elif randNo == 3:
    comp = 'p'
you = input('your turn : rock(r), paper(p), scissor(s)? :')
output = gameWin(comp, you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if output == None:
    print("the gane is tie!")
elif output:
    print("You Win!!")
else:
    print("you lose!!")

