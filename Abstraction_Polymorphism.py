class india():
    def capital(self):
        print("the capital of India is Delhi")
    def language(self):
        print("the primary language is Hindi")
    def type(self):
        print("India is a developing country")
class usa():
    def capital(self):
        print("the capital of USA is Washington DC")
    def language(self):
        print("the primary language is English")
    def type(self):
        print("USA is a developing country")
ob_ind=india()
ob_usa=usa()
for items in (ob_ind,ob_usa):
    items.capital()
    items.language()
    items.type()

from abc import ABC,abstractmethod
class animal(ABC):
    def quality(self):
        pass
class dog(animal):
    def quality(self):
        print("I can bark")
class snake(animal):
    def quality(self):
        print("I can crawl")
class lion(animal):
    def quality(self):
        print("I can roar")
d=dog()
d.quality()
l=lion()
l.quality()
s=snake()
s.quality()