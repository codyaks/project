num=int(input("please enter the number"))
p=int(input("please enter the power"))
sum=num
for i in range(1,p):
    sum=sum*num
print("the power",sum)