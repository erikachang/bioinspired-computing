"""genetic_programming.py

This file stands for the genetic programming class
that is used to execute the algorithm itself. It
contains genetic operators (such as crossover and
mutation).
"""

import random;
import genetic_operators;
import utils;
from random import randint
import copy

class GeneticProgramming:

    def __init__(self,populationSize,maxGenerations,elitismPercentage=0.1,crossoverProbability=0.5,tournamentSize=5,mutationPercentage=0.05,mutationProbability=0.03):
        """
        "Constructor" of the class. Initializes the main components and parameters
        of the Genetic Program.

        :param populationSize:       population size of each generation.
        :param maxGenerations:       max number of generations in the execution.
        :param elitismPercentage:    percentage of the population that will be considered elite, which will be
                                     added directly to the next population. Default value is 0.1 (10%).
        :param crossoverProbability: probability of occurring crossover. Default value is 0.5 (50%).
        :param tournamentSize:       the size of the tournament, which is responsible for choosing the parents
                                     that will be used in the crossover. Default value is 5 (5 participants).
        :param mutationPercentage:   related to the percentage of the population that will be mutated in each
                                     generation. Default value is 0.05 (5%).
        :param mutationProbability:  probability of occurring mutation in a given individual. Default value is
                                     0.03 (3%).
        """
        # Funcoes
        self.functions = [n.value for n in utils.LevelPositionTypes];

        # Terminais
        self.terminals = [n.value for n in utils.Moves];
	#self.terminals = ['R','J','F'];

	# Population
        self.population = [];
	self.best = None;

        # Tamanho da populacao
        self.populationSize =  populationSize

        # Numero maximo de geracoes
        self.maxGenerations = maxGenerations;

        # Percentual de Elitismo
        self.elitismPercentage = elitismPercentage;

        # Probabilidade de Ocorrencia de  Croosover
        self.crossoverProbability = crossoverProbability;

        # Tamanho do torneio
        self.tournamentSize = tournamentSize;

        # Probabilidade de Ocorrencia de Mutacao 
        self.mutationPercentage = mutationPercentage;

        # Probabilidade de Mutacao dos nodos
        self.mutationProbability = mutationProbability;

    def generatePopulation(self, tree, left):
	if left == 1:
	    tree.value = self.terminals[randint(0,2)]
	    #print "treeVAlE", tree.value
	    return
	if randint(0,1) <  1:
	    tree.value = self.terminals[randint(0,2)]
	    #print "treeVAlD", tree.value
	    return

	tree.left = utils.Tree()
	tree.right = utils.Tree()
	
	tree.value = self.functions[randint(0,2)]
	#print "treeVAlDFunc", tree.value

        self.generatePopulation(tree.left, 1)
	self.generatePopulation(tree.right, 0)

    def generateInitialPopulation(self):
        """
        Generates the initial population of the evolution
        """
        # Codigo para geracao da populacao inicial
	for x in range(self.populationSize):
  	    novo = utils.Tree()
	    novo.left = utils.Tree()
            novo.right = utils.Tree()
            novo.value = self.functions[randint(0,2)]
            self.generatePopulation(novo.left, 1)
            self.generatePopulation(novo.right, 0)
            self.population.append(novo)
            #print "----INSERINDO:", novo.value
            del(novo)

    def getNextGeneration(self):
	"""
	Generates Next Generation 
	
	- Executa CrossOver
	- Executa Elitismo
	- Executa Mutacoes
	
	"""

	#print "---- GET NEXT GEN"


    	#ELETISMO
    	nextPopulation = genetic_operators.executeEletismo(self.population, self.elitismPercentage)
        
    	#MUTACAO
	eliteSize = self.elitismPercentage*self.populationSize
        for x in range(int(self.mutationPercentage*len(self.population))):
            
            aux = randint(eliteSize,len(self.population)-1)
            #print ">>", aux, len(minhaPopulacao)
            individual = self.population[aux]
            self.population.pop(self.population.index(individual))

            children = genetic_operators.executeMutation(individual, self.functions, self.terminals, self.mutationProbability)
	    #print children.value
	    nextPopulation.append( children )
	
    	#CROSS
	#minhaPopulacao = copy.deepcopy(self.population);
	for x in range(int(len(nextPopulation)-self.populationSize)):
	
		parentTupla = genetic_operators.getParentByTournament(self.population, self.tournamentSize)
		children = genetic_operators.executeCrossover(parentTupla[0], parentTupla[1], self.crossoverProbability)
		nextPopulation.append(children[0])
		nextPopulation.append(children[1])

        #matem a mesmo tamanho de populacao
	'''minhaPopulacao.sort(key=lambda parent:parent.fitness)
	minhaPopulacao.reverse()
	minhaPopulacao.pop(0)
	minhaPopulacao.pop(0)'''

	#genetic_operators.????? ELITISMO ???????
    
	    #print "---- FIM GET NEXT GEN"

        


	#matem a mesmo tamanho de populacao
	'''minhaPopulacao.sort(key=lambda parent:parent.fitness)
	minhaPopulacao.reverse()
	minhaPopulacao.pop(0)'''

	return nextPopulation;

    def run(self):
	#print "-----RUN"
        """
        Executes the genetic program.
        :return: the best individual (solution) found to the problem.
        """

        numGenerations = 0;
	
	best = utils.Tree()

        while(numGenerations < self.maxGenerations):
	    #print "-----GERACAO:", numGenerations
            if(numGenerations == 0):
		self.generateInitialPopulation();
            else:
                self.population = self.getNextGeneration();

            #Calcula Fitness de Toda a Populacao
            for current in self.population:
            
                current.fitness = utils.calculateFitness(current);
            	
		print "Fitness curr:", current.fitness, "best:", best.fitness
                if best.fitness > current.fitness:
                    best = current;
                elif best.fitness == current.fitness :
                    if utils.Tree.getTreeSize_rec(best) > utils.Tree.getTreeSize_rec(current):
                        best = current
            #Finally...
            numGenerations += 1;
        
	best.printable()

	return best;



'''def MeuTest():
    populationSize = 100;
    maxGenerations = 100;

    gp = GeneticProgramming(populationSize, maxGenerations);

    novo = utils.Tree()
    #print gp.maxGenerations
    gp.generatePopulation(novo, 0)
    gp.population.append(novo)
    #print "----INSERINDO:", novo.value

    novo = utils.Tree()
    #print gp.maxGenerations
    gp.generatePopulation(novo, 0)
    gp.population.append(novo)
    #print "----INSERINDO:", novo.value

    novo = utils.Tree()
    #print gp.maxGenerations
    gp.generatePopulation(novo, 0)
    gp.population.append(novo)
    #print "----INSERINDO:", novo.value

    novo = utils.Tree()
    #print gp.maxGenerations
    gp.generatePopulation(novo, 0)
    gp.population.append(novo)
    #print "----INSERINDO:", novo.value
    for current in gp.population:       
	current.fitness = utils.calculateFitness(current);

    for current in gp.population:       
	#print "f", current.fitness

    #genetic_operators.getParentByTournament(gp.population, 2)

    #genetic_operators.executeCrossover(gp.population[0], gp.population[1], 101)

if __name__ == "__main__" :
    MeuTest()
'''
