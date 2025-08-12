dic1={"codingal":1,"is":1,"best":2,"for":1,"coding":2}
check=int(input("please enter the no. you want to check(1 or 2)"))
num=0
for keys in dic1:
    if check==dic1[keys]:
        num=num+1
print("the frequency of the number",check,"is",num)