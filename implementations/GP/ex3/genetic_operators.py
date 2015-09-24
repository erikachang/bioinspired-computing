__author__ = 'Thomas'
from random import randint
import copy

def getParentByTournament(population, tournamentSize):
    # create a tournament between the population's individuals
    # return two winners

    tournamentPopulation = []
    populationSize = len(population)
    poolSize = 0
    # get individuals randomly according to tournamentSize
    while poolSize < tournamentSize:
        candidate = population[randint(0, populationSize-1)]
        if candidate not in tournamentPopulation:
            tournamentPopulation.append(candidate)
            poolSize += 1
        
    # sort individuals by fitness
    tournamentPopulation.sort(key=lambda parent:parent.fitness)
    # return the individuals with lowest fitness
    return (tournamentPopulation[0], tournamentPopulation[1])

def items(tree):
    # return the total items of a tree

    if tree is None:
        return 0

    total = 1
    total += items(tree.left)
    total += items(tree.right)

    return total

def navigate(tree, size):
    # navigate through the tree until size
    # return the tree from size 

    if tree is None :
       return (None, size)

    if size-1 == 0 :
       return (tree, size-1)

    left = navigate(tree.left, size-1)
    
    if left[0] is not None:
       return left

    right = navigate(tree.right, left[1])
    
    if right[0] is not None:
        return right

    return (None, right[1])
     
def elitism(population, rate):
    # return a set with the k best individuals from population

    # sort individuals by fitness
    population.sort(key=lambda parent:parent.fitness)
    
    return population[:int(rate*len(population))]

def crossover(parent1, parent2, rate):
    """
    Executes crossover between two parents

    :param parent1: the first parent to be used in crossover
    :param parent2: the second parent to be used in crossover
    :return         generated children (child1 and child2)
    """

    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    boolRate = randint(0, 100)

    # measure the crossover rate
    if boolRate < rate :
        
        # initialize parents for crossover
        parent1Elem = items(parent1)
        parent2Elem = items(parent2)

        randParent1 = randint(0, parent1Elem/2-1)
        randParent2 = randint(0, parent2Elem/2-1)

        # original
        p1 = navigate(parent1, randParent1*2+1)
        p2 = navigate(parent2, randParent2*2+1)

        # copy
        c1 = navigate(child1, randParent1*2+1)
        c2 = navigate(child2, randParent2*2+1)
    
        # transfer
        c1[0].left = copy.deepcopy(p2[0].left)
        c1[0].right = copy.deepcopy(p2[0].right)
        c1[0].value = p2[0].value
    
        c2[0].left = copy.deepcopy(p1[0].left)
        c2[0].right = copy.deepcopy(p1[0].right)
        c2[0].value = p1[0].value
        
    return child1, child2


def mutation(individual, functions, terminals, mutationProbability):
    """
    Executes the mutation of a given individual to create a new one

    :param individual: the individual (node) that will be mutated
    :param functions:  the functions that are going to be mutated
    :param terminals:  the terminals that are going to be mutated
    :return:           the new individual
    """

    newIndividual = copy.deepcopy(individual)

    while randint(0,100) < mutationProbability:
        # get elements from individual
        indElem = items(newIndividual)
        # get a random element
        randInd = randint(1,indElem)
    
        # reach the random element in the individual
        c1 = navigate(newIndividual, randInd)
    
        # mutate the element according to its definition (function/terminal)
        if c1[0].value in functions :
            c1[0].value = functions[randint(0,2)]
        else:
            c1[0].value = terminals[randint(0,2)]

    return newIndividual
