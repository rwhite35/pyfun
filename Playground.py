#
# Playground - a safe space for new learnings!
# author: ronwhite562@gmail.com
# v1.0, 20240525
  

## the Tyranny of Ternaries
# Apples single byte:  min = "a" if a < b else "b"
# Berries nested ops:  min = "a" if a > b else "c" if c < b else "b"
#
option = ["red","blue","green"]

class Apple:
    color = ""

    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.color = self.oneByte(option)

    def oneByte(self,option) -> str:
        return option[0] if self.r > self.b else option[2]
    

class Berry:
    color = ""

    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.color = self.twoBerries(option)

    def twoBerries(self,option) -> str:
        return option[0] if self.r > self.b else option[1] if self.g < self.b else option[2]
    

firstChoice = Apple(4,6,8)
lastChoice = Berry(4,6,8)
print("My Apples are " + firstChoice.color + " over " + lastChoice.color + " Berries!")


# Duck Duck Witch
# Duck Typing works on the principle that one object can be replace another 
# as long as each class implements some of the same methods and attributes.  
# The method matters for duck sake. More than the object that defined it!
# 
# Pythons interpreter replaces the original object at runtime as long as a 
# common method or attribute exists in the replacement object.
#
# Strickly speaking, dynamically typed languages implement the Liskov
# substitution priciple with less grief than their strong typed counterparts.
#
class Duck:
    def canFloat(self):
        print("Ducks float!")

class Newt:
    def canFloat(self):
        print("Newts fly!")

class Trial:
    def reasoning(self, duck):
        print("What else floats like wood?")
        duck.canFloat()


# if walks like a Duck and quacks like a Duck, 
# it must be a witch!
ducks = Duck()
newts = Newt()

witches = Trial()
witches.reasoning(newts)
witches.reasoning(ducks)