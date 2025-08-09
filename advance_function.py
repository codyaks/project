lst1=[1,3,5]
lst2=[2,4,6]
result=map(lambda x, y: x +y,lst1,lst2)
print(list(result))

num=[2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num))
print(square)

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
      print(x,y)

stock=["tata","mrf","wipro"]
price=[1000,5000,500]
newdic={stock:price for stock,price in zip(stock,price)}
print(newdic)