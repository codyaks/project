import random
x="abcdefghijklmnopqrstuvwxyz"
sp=["!","@","#","$","%","^","&","*"]
password=""
num=()
r=random.randrange(5,6)
r1=random.randrange(4,5)
r2=random.randrange(2,3)
for i in range(0,r):
    password=random.choice(x)+password
for i in range(0,r1):
    num=random.randint(0,9)
    strnum=str(num)
    password+=strnum
for i in range(r2):
    x=random.choice(sp)
    password+=x
lstp=list(password)
lpassword=random.sample(lstp,len(lstp))
fpassword="".join(lpassword)
print(fpassword)
