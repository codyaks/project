import random
print("welcome to the game",)
def setup():
    print("please choose the difficulty level from option 1, 2 or 3")
    mode=int(input("please enter the difficulty level of the game(1/2/3)-"))
    if mode==1:
        game_1()
    elif mode==2:
        game_2()
    elif mode==3:
        game_3()

def game_1():
    print("you have choosen the first level\n you have to choose from 1 to 5")
    num=random.randint(1,5)
    userin=int(input("please enter your choice-"))
    if num==userin:
        print("you have choosen the correct number congrats")
    else:
        print("you have choosen the wrong number.the correct number was",num)
    res=input("do you want to play again Y/N")
    if res=="y"or"Y":
        setup()

def game_2():
    print("you have choosen the second level\n you have to choose from 1 to 10")
    num=random.randint(1,10)
    userin=int(input("please enter your choice-"))
    if num==userin:
        print("you have choosen the correct number congrats")
    else:
        print("you have choosen the wrong number.the correct number was",num)
    res=input("do you want to play again Y/N")
    if res=="y"or"Y":
        setup()

def game_3():
    print("you have choosen the third level\n you have to choose from 1 to 15")
    num=random.randint(1,15)
    userin=int(input("please enter your choice-"))
    if num==userin:
        print("you have choosen the correct number congrats")
    else:
        print("you have choosen the wrong number.the correct number was",num)
    res=input("do you want to play again Y/N")
    if res=="y"or"Y":
        setup()
setup()