class dog:
    species="dog"
    def __init__(self,breed,colour,age):
        self.breed1=breed
        self.colour1=colour
        self.age1=age
tommy=dog("bulldog","brown",7)
Daisy=dog("German Shepherd","black",10)
Charlie=dog("Labrador Retriever","golden brown",5)

print("the species of tommy is-",tommy.species)
print("the species of Charlie is-",Charlie.species)
print("the species of Daisy is-",Daisy.species)

print("the breed of tommy is-{} , and its colour is-{} and age is-{}".format(tommy.breed1,tommy.colour1,tommy.age1))
print("the breed of daisy is-{} , and its colour is-{} and age is-{}".format(Daisy.breed1,Daisy.colour1,Daisy.age1))
print("the breed of charlie is-{} , and its colour is-{} and age is-{}".format(Charlie.breed1,Charlie.colour1,Charlie.age1))
