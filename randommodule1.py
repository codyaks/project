import random
print("guess the number game")
num=random.randint(20,30)
print("in this game you have to guess a number between 20 to 30")
while True:
    guess=int(input("please enter the number"))
    if num==guess:
        print("you have choosen the right number")
        print("the number was-",num)
        break
    else:
        print("you have choosen the wrong number")
        print("try again")