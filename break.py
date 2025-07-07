word=input("please enter a word")
l=input("please enter a letter")
w=word.lower()
letter=l.lower()
flag=True
for i in w:
    if (i==letter):
        flag=False
        break
if flag==False:
    print(letter,"is found")   
    
else:
    print(letter,"is not found")  

var=10
while var>0:
    var=var-1
    if var==5:
        continue
    print(var)

num=int(input("please enter a number"))
if num%2==0:
    print("fizz")
elif num%15==0:
    pass
elif num%10==0:
    print("happy")
elif num%5==0:
    print("hey")
else:
    print(num)