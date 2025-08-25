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