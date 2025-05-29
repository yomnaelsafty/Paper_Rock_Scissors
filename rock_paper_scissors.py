import random

a = input("do you whant to play agame? ")
x = ["paper","scissers","rock"]

if a == "yes":
    print("let's start")
    user_choice = input("chosse paper or scissers or rock : ")
    pc_choice = random.choice(x)
    print("pc chosse is :" + pc_choice )
    if user_choice == pc_choice:
        print ("it's a tie")
    elif user_choice == "paper" and pc_choice ==" rock":
        print("you win")
    elif user_choice == "rock" and pc_choice == "scissers":
        print("you win")
    elif user_choice == "scissers" and pc_choice == "paper":
        print("you win")
    else:
        print("you lose")
elif a == "no":
    print("it's oky, nice to meet you")
else:
    print("can't understand the anther")
