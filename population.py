import creature
import random

def map(x, min1, max1, min2, max2):
    return (x-min1)/(max1-min1)*max2

eps = 0.01

class Population:
    def __init__(self, mutationRate, eq, num):
        self.mutationRate = mutationRate        
        self.eq = eq
        self.population = []
        for i in range(num):
            self.population.append(creature.Creature(eq))
        self.computeFitness()
        self.matingPool = []    
        self.finish = False      #finish evolving?? 
        self.generations = 0     #number of generation
        
    def computeFitness(self):
        for i in range(len(self.population)):
            self.population[i].computeFitness()
            
    def selection(self):
        self.matingPool.clear()
        self.population.sort(key=lambda creature: creature.fitness, reverse=True) 
        for i in range(1, len(self.population)):
            if(i == 1 or self.population[i].fitness != self.population[i-1].fitness):
                for j in range(i):
                    self.matingPool.append(self.population[i])
    
    def generate(self):
        for i in range(len(self.population)):
            a = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
            b = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
            child = a.crossover(b)
            child.mutate(self.mutationRate)
            self.population[i] = child
        self.generations += 1
    
    def getBest(self):
        best = self.population[0].fitness
        index = 0
        for i in range(len(self.population)):
            if(self.population[i].fitness < best):
                best = self.population[i].fitness
                index = i
        
        if(best < eps):
            self.finish = True
        return self.population[index]
    
        
    def finished(self):
        return self.finish

    def getGenerations(self):
        return self.generations
