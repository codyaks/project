class dad:
    def __init__(self,eyes,aggressive):
        self.eyes=eyes
        self.aggressive=aggressive
    def print1(self):
        print("your eyes colour is ",self.eyes)
        print("your are aggressive",self.aggressive)
class son(dad):
    def __init__(self, eyes, aggressive,age,name):
        self.name=name
        self.age=age
        super().__init__(eyes, aggressive)
obj=son("blue","true","6","tommy")
print("name is ",obj.name,"and age is",obj.age)

obj.print1()

class vehicle:
    def __init__(self,max_speed,milege,name):
        self.max1=max_speed
        self.name=name
        self.milege=milege
class bus(vehicle):
    pass
bus1=bus(80,"15km/L","volvo")
print("milege is-",bus1.milege)
print("max speed is-",bus1.max1)
print("name is-",bus1.name)