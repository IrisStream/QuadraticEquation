import population
import equation
import creature

eq = equation.Equation(1.0, -7.0, 12.0)
mutationRate = 0.1
populationSize = 200

GApopulation = population.Population(mutationRate, eq, populationSize)

while (GApopulation.finished() == False):
    GApopulation.selection()
    
    GApopulation.generate()

    GApopulation.computeFitness()
    
    print(GApopulation.getBest().getBits())
    


print(GApopulation.getBest().getNum())