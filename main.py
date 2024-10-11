from random import *

def printWithAddLength(string,number):
    s = string
    offset = number - len(s)
    for _ in range(offset):
        s+=" "
    print(s,end = " ")

class Number:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        self.number = randint(1, 10)

    def __str__(self):
        return f"{self.number}"

    def printMinusOnly(self):
        if self.sign == "+":
            return f"{self.number}"
        else:
            return f"{self.sign}{self.number}"

    def printWithSign(self):
        return f"{self.sign}{self.number}"

    def printNoSign(self):
        return f"{self.number}"


class Sign:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        return f"{self.sign}"


class Var:

    def __init__(self):
        self.number = randint(1, 10)
        self.letter = "x"
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        temp = ""
        if self.sign != "+":
            temp += "-"
        if self.number != 1:
            temp += str(self.number)
        return f"{temp}{self.letter}"


class Function:

    def __init__(self,countX):
        self.x = Var()
        self.sign = Sign()
        self.b = Number()
        self.y = 0
        self.xs = []
        for i in range(countX):
            self.xs.append(randint(-10, 10))

    def __str__(self):
        return f"y = {self.x} {self.sign} {self.b}"


n = 20
for x in range(n):
    f = Function(3)
    printWithAddLength(str(f),15)
    print(f"x={f.xs}")
