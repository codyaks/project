n=int(input("please enter the no. you want to add"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum=",sum)
#loop for string value reversal
str1=input("please enter the str value you want to reverse")
str2=""
for i in str1:
    str2=i+str2
print("the orignal string is-",str1)
print("the reversed string is-",str2)
#loop for reversed no.
num1=int(input("please enter the value"))
print("the numbers from {0} to {1} are".format(num1,1))
for i in range(num1,0,-1):
    print("reversed no. are",i)