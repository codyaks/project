import random
while True:
    print("lets play rock, paper, scissor game")
    userin=input("please enter your choice (rock, paper or scissor)")
    possibleop=["rock","paper","scissor"]
    compin=random.choice(possibleop)
    if userin==compin:
        print("tie! both choices was same")
    elif userin=="rock":
        if compin=="paper":
            print("paper covers the rock you lost the game")
        else:
            print("rock snapes the scissor you won the game")
    elif userin=="paper":
        if compin=="rock":
            print("paper covers the rock you won the game")
        else:
            print("scissor cuts the paper you lost the game")
    elif userin=="scissor":
        if compin=="paper":
            print("scissor cuts the paper you won the game")
        else:
            print("rock snapes the scissor you lost the game")
    play=input("do you want to play again y/n-")
    if play!="y":
        break
