import random
def game(comp,you):
    if you > 50:
        print("Choose less than 50 ")
    else:
        if comp == you:
            print("Hurray, you and computer chooses a same number ")
        elif comp > you:
            print("Choose a greater number ")
        else:
            print("Choose a lower number ")
print("Computer choose ")
comp = random.randint(1,50)

you = int(input("Choose a number from 1 to 50 : "))
print(f"Computer chooses {comp}")
print(f"You choose {you}")
choose = game(comp,you)