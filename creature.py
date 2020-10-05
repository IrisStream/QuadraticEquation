import math
import random
from codecs import decode
import struct
import equation

def floatToBits(num):
     return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

def bitsToFloat(num):
    f = int(num,2)
    return struct.unpack('f',struct.pack('I',f))[0]

class Creature:
    def __init__(self, eq):
        self.adn = ''
        self.fitness = 0.0
        self.eq = eq
        for i in range(32):
            self.adn += random.choice(['0','1'])
    
    def getNum(self):
        return bitsToFloat(self.adn)

    def computeFitness(self):
        self.fitness = abs(self.eq.computeValue(self.getNum()))        

    def getBits(self):
        return self.adn

    def crossover(self,partner):
        child = Creature(self.eq)
        midPoint = random.randrange(0,32)
        child.adn = ''
        for i in range(32):
            if(i < midPoint):
                child.adn += self.adn[i]
            else:
                child.adn += partner.adn[i]
        return child

    def mutate(self, mutationRate):
        adn = ''
        for i in range(32):
            if(random.random() < mutationRate):
                adn += random.choice(['0','1'])
            else:
                adn += self.adn[i]
        self.adn = adn