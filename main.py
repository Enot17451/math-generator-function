from random import *

class Number:
    
    def __init(self):
        self.sign = choice(["+","-","+","-","+","-","+","-","+","-","+","-"])
        self.number = randint(1,10)
        
    def printMinusOnly():
        if self.sign == "+":
            return f"{self.number}"
        else:
            return f"{self.sign}{self.number}"
        
    def printWithSign(self):
        return f"{self.sign}{self.number}"
    
    def printNoSign(self):
        return f"{self.number}"
        
class Sign:
    
    def __init(self):
        self.sign = choice(["+","-","+","-","+","-","+","-","+","-","+","-"])
        
    def __str__(self):
        return f"se"
        
class Var:
    
    def __init__(self):
        self.number = randint(1,10)
        self.letter = "x"
        self.sign = choice(["+","-","+","-","+","-","+","-","+","-","+","-"])        
    

class Function:
    
    def __init__(self):
        self.x = Var()
        self.sign = Sign()
        self.b = Number()
        self.y = 0
        
    def __str__(self):
        return f"y = {self.x} {self.sign} {self.b}"

n = 10
for x in range(n):
    print(Function())
