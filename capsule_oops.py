class price:
    def __init__(self):
        self.__maxprice=900
    def print1(self):
        print("the max price is-",self.__maxprice)
    def set_price(self,price):
        self.__maxprice=price
c=price()
c.print1()
c.__maxprice=1000
c.print1()
c.set_price(1000)
c.print1()
class myclass:
    __pvar=23
    def __pfun(self):
        print("I am in the class")
    def print2(self):
        print(myclass.__pvar)
        self.__pfun()
f=myclass()
f.print2()

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return"({},{})".format(self.x,self.y)
p=point(2,4)
print(p)