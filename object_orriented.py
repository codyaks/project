class parrot:
    species="parrot"

    def __init__(self,name,age):
        self.myname=name
        self.age=age

woo=parrot("woo",5)
blu=parrot("blu",8)

print("the species of woo is",woo.species)
print("the species of woo is",blu.species)
print("the name and age of the the first parrot is-",woo.myname,woo.age)
print("the name and age of the the sceond parrot is-",blu.myname,blu.age)