row=int(input("please enter the rows"))
space=row-1
dot=row-space
for n in range(1,row+1):
    for f in range(space):
        print(end=" ")
    for j in range(dot):
        print("6*",end=" ")
    space=space-1
    dot=dot+1
    print()