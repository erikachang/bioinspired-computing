__author__ = 'Thomas'
from random import randint
import copy

def getParentByTournament(population, tournamentSize):
    tournamentPopulation = [];

    #Digite aqui o codigo para a escolha dos pais por torneio
    #pega 4 elementos aleatorios da populacao
    for x in rand(0,3):
	randParent = randint(0, tournamentSize)
	tournamentPopulation.append( population[randParent] )
    
    #ordena os 4 elementos pelo fitness
    tournamentPopulation.sort(key=lambda, parent:parent.fitness)

    #retorna o de maior fitness
    return tournamentPopulation[0];

def profundidade(tree):
    if tree == None :
        return 0
    
    esquerda = profundidade(tree.left) + 1

    direita = profundidade(tree.right) + 1

    maior = esquerda
    if maior < direita :
	maior = direita

    return maior

def itens(tree):
    if tree == None :
        return 0

    soma = 1

    soma += itens(tree.left)

    soma += itens(tree.right)

    return soma

def navega(tree, size) :
    if size-1 == 0 :
	return (tree, size-1)
    left = navega(tree.left, size-1)

    if left[0] != None :
	return left

    right = navega(tree.right, left[1]-1)

    if right[0] != None : 
	return right

    return (None, right[1]-1)

    

     

def executeCrossover(parent1, parent2, taxaCross):
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
    boolTaxa = randint(0, 100)

    boolTroca = False

    #medicao da taxa de cross
    if boolTaxa < taxaCross :
	
	#inicializa variaveis
	parent1Elem = itens(parent1)

        parent2Elem = itens(parent2)

        randParent1 = randint(0, parent1Elem)

        randParent2 = randint(0, parent2Elem)
	
	#original
        p1 = navega(parent1, randParent1)

        p2 = navega(parent2, randParent2)

	#copia
	c1 = navega(child1, randParent1)
	
 	c2 = navega(child2, randParent2)

	#transferindo
	c1[0].left = copy.deepcopy(p2[0].left)

	c1[0].right = copy.deepcopy(p2[0].right)

	c2[0].left = copy.deepcopy(p1[0].left)

	c2[0].right = copy.deepcopy(p1[0].right)

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
