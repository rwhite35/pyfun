#
# Playground - a safe space for new learnings!
# author: ronwhite562@gmail.com
# v1.0, 20240525
  

## the tyranny of Ternaries
# Apples single byte:  min = "a" if a < b else "b"
# Berries many options:  min = "a" if a > b else "c" if c < b else "b"
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


## Duck Duck Witch
# Duck Typing works on the principle that one object can replace by another 
# - as long as each implement some of the same methods and/or attributes.  
# 
# At runtime, the interpreter can replace the original compiled object 
# as long as the method or attribute is also available in the runtime replacement.
# The methods matter for duck sake!
#
# `Strickly speaking` (ahem), dynamically typed languages implement the Liskov
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


# If it walks like a Duck, and quacks like a Duck... 
# It must be a witch!
ducks = Duck()
newts = Newt()

witches = Trial()
witches.reasoning(newts)
witches.reasoning(ducks)