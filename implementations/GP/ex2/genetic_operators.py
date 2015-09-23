__author__ = 'Thomas'
from random import randint
import copy

def getParentByTournament(population, tournamentSize):
    tournamentPopulation = [];
    

    #Digite aqui o codigo para a escolha dos pais por torneio
    #pega 4 elementos aleatorios da populacao
    for x in range(tournamentSize):
	randParent = randint(0, len(population)-1)
	tournamentPopulation.append( population[randParent] )
    
    #ordena os 4 elementos pelo fitness
    tournamentPopulation.sort(key=lambda parent:parent.fitness)

    #retorna o de menor fitness
    return (tournamentPopulation[0], tournamentPopulation[1]);

def itens(tree):
    if tree == None :
        return 0

    soma = 1

    soma += itens(tree.left)

    soma += itens(tree.right)

    return soma

def navega(tree, size) :
    if tree == None :
	return (None, size)

    #print (tree.value, size)

    if size-1 == 0 :
	return (tree, size-1)

    left = navega(tree.left, size-1)
    if left[0] != None :
	return left

    right = navega(tree.right, left[1])
    if right[0] != None : 
	return right

    return (None, right[1])
    

     
def executeEletismo(population, rate):
    #newPopulation = population

    population.sort(key=lambda parent:parent.fitness)
    
    return population[:int(rate*len(population))]

def executeCrossover(parent1, parent2, rate):
    """
    Executes crossover between two parents

    :param parent1: the first parent to be used in crossover
    :param parent2: the second parent to be used in crossover
    :return         generated children (child1 and child2)
    """

    child1 = copy.deepcopy(parent1);
    child2 = copy.deepcopy(parent2);

    #Digite aqui o codigo para a realizacao do crossover
    # define um sorteio entre 0 e 100 para se fazer a medicao da taxa de CROSS
    boolRate = randint(0, 100)

    boolTroca = False

    #child1.printable()
    #child2.printable()

    #medicao da taxa de cross
    if boolRate < rate :
	
	#inicializa variaveis
	parent1Elem = itens(parent1)

        parent2Elem = itens(parent2)

        randParent1 = randint(0, parent1Elem/2-1)

        randParent2 = randint(0, parent2Elem/2-1)

	#print "RAND P1,", randParent1, "RAND P2,", randParent2
	
	#original
        p1 = navega(parent1, randParent1*2+1)

        p2 = navega(parent2, randParent2*2+1)

	#copia
	c1 = navega(child1, randParent1*2+1)
	
 	c2 = navega(child2, randParent2*2+1)

	#transferindo
	#print ">>>>>", c1[0]
	#print ">>>>>", p1[0]
	#print ">>>>>", p2[0]
	#c1[0] = copy.deepcopy(p2[0])
	c1[0].left = copy.deepcopy(p2[0].left)

	c1[0].right = copy.deepcopy(p2[0].right)

	c1[0].value = p2[0].value

	#c2[0] = copy.deepcopy(p1[0])
	c2[0].left = copy.deepcopy(p1[0].left)

	c2[0].right = copy.deepcopy(p1[0].right)

	c2[0].value = p1[0].value

    #child1.printable()
    #child2.printable()

    return child1, child2;


def executeMutation(individual, functions, terminals, taxaMutacao):
    """
    Executes the mutation of a given individual to create a new one

    :param individual: the individual (node) that will be mutated
    :param functions:  the functions that are going to be mutated
    :param terminals:  the terminals that are going to be mutated
    :return:           the new individual
    """

    newIndividual = copy.deepcopy(individual);

    #Digite aqui o codigo para a realizacao da mutacao
    
    while randint(0,100) < taxaMutacao :
        indElem = itens(newIndividual)
	
	randInd = randint(1,indElem)
	
	c1 = navega(newIndividual, randInd)
	
	if c1[0].value in functions :
	    c1[0].value = functions[randint(0,2)]
	else:
	    c1[0].value = terminals[randint(0,2)]

	

    return newIndividual;