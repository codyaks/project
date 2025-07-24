tuple1=(1,3,"hi",2.34,True)
print(tuple1)

tuplex=(1,2,3,4,5)
print(tuplex)
tuplex=tuplex+(6,)
print(tuplex)

tuple2=(20,20,30,40,50,20,21)
print(tuple2.count(20))

tuple3=(2,6,4,8,2,9,6,3,0)
slice1=tuple3[2:6]
print(slice1)
slice2=tuple3[:3]
print(slice2)

def palin(r):
    s=0
    e=len(r)-1
    while s<e:
       if r[s]==r[e]:
            s+=1
            e-=1
       else:return False
    return True
r=(1,2,3,3,2,1)
if(palin(r)):
    print("its a palindrome")
else:
    print("its not a palindrome")

count=(1,1,1,0,0,1,0,0,0)
r=0
s=0
for i in count:
    if i==1:
        s+=1
    else:
        r+=1
if r>s:
    print("its a rainy day")
else:
    print("its a sunny day")