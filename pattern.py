print("triangle star pattern")
n=int(input("please enter the number of rows-"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")

#pattern with numbers
print("triangle star pattern")
l=int(input("please enter the number of rows-"))
for v in range(l):
    for k in range(v+1):
        print(v,end="")
    print("")

print("triangle star pattern")
l=int(input("please enter the number of rows-"))
for v in range(l):
    for k in range(v+1):
        print(k+1,end="")
    print("")

print("triangle star pattern")
l=int(input("please enter the number of rows-"))
i=1
for v in range(l):
    for k in range(v+1):
        print(i,end=" ")
        i=i+1
    print("")

#daimond shape
row=int(input("please enter the number of rows as odd no."))
hd=int(row/2)+1
space=hd-1
for i in range(1,hd+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    for j in range(2*i-1):
        print("*",end=" ")
    print()