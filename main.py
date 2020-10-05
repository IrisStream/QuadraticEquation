import population
import equation
import creature

eq = equation.Equation(1.0, 2.0, -2.0)
mutationRate = 0.1
populationSize = 100

GApopulation = population.Population(mutationRate, eq, populationSize)

while (GApopulation.finished() == False):
    GApopulation.selection()
    
    GApopulation.generate()

    GApopulation.computeFitness()
    
    print(GApopulation.getBest().getBits())
    


print(round(GApopulation.getBest(), 4))