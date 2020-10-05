import math

class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.low = self.extrama() - 500.0
        self.high = self.extrama() + 500.0

    def computeValue(self, x):
        if(math.isnan(x) or x > self.high):
            x = self.high
        if(x < self.low):
            x = self.low
        return ((self.a * x * x) + (self.b * x) + self.c)
    
    def extrama(self):
        return (-self.b)/(self.a * 2)