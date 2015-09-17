__author__ = 'Thomas'
from random import randint

def getParentByTournament(population, tournamentSize):
    tournamentPopulation = [];

    #Digite aqui o codigo para a escolha dos pais por torneio
    for x in rand(0,3):
	randParent = randint(0, tournamentSize)
	tournamentPopulation.append( population[randParent] )

    tournamentPopulation.sort(key=lambda, parent:parent.fitness)

    return tournamentPopulation[0];

def executeCrossover(parent1, parent2, taxaCross):
    """
    Executes crossover between two parents

    :param parent1: the first parent to be used in crossover
    :param parent2: the second parent to be used in crossover
    :return         generated children (child1 and child2)
    """

    child1 = None;
    child2 = None;

    #Digite aqui o codigo para a realizacao do crossover
    boolTaxa = randint(0, 100)

    if boolTaxa < taxaCross :
	print "TODO - crossover"


    return child1, child2;


def executeMutation(individual, functions, terminals):
    """
    Executes the mutation of a given individual to create a new one

    :param individual: the individual (node) that will be mutated
    :param functions:  the functions that are going to be mutated
    :param terminals:  the terminals that are going to be mutated
    :return:           the new individual
    """

    newIndividual = None;

    #Digite aqui o codigo para a realizacao da mutacao

    return newIndividual;
