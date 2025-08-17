newlst=[]
fruits=["apple","mango","guave"]
for fruit in fruits:
    new=fruit.capitalize()
    newlst.append(new)
print(newlst)
for i in range(10):
    if i==6:
        print("exit")
        exit()
    print(i)
