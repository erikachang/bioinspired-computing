"""utils.py

This file stands for helper functions to be used
when evaluating the level vector.
"""

from enum import Enum
import sys

level = ['P','P','P','H','H','P','P','P','H','P','P','P','P','H','P','P','E','E','P','P'];	

class LevelPositionTypes(Enum):
    plain = 'P'
    hole = 'H'
    enemy = 'E'

class Moves(Enum):
    right = 'R'
    jump = 'J'
    fire = 'F'
	
class Tree():
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None   #LevelPositionTypes(Node) OR Moves(Terminal)
    	self.fitness = float("INF")    #Fitness

    
    def getTreeSize_rec(tree):
	
	if (tree.value in [n.value for n in Moves]):
	    return 1;
	
	left = 0;
	right = 0;
	
	if (tree.left != None):
	    left = Tree.getTreeSize_rec(tree.left);
		
	if (tree.right != None):
	    right = Tree.getTreeSize_rec(tree.right);

	return left + right + 1;
	
    def getTreeSize(self):
	"""
	Return size of the Tree
	"""
	#return Tree.getTreeSize_rec(self);
	pass

    def profundidade(tree):
	if tree == None :
	    return 0
	    
	esquerda = profundidade(tree.left) + 1

	direita = profundidade(tree.right) + 1

	maior = esquerda
	if maior < direita :
	    maior = direita

	return maior
    
    def printable2(self, tree):
	if tree == None :
            return 0

	print tree.value

	print "Esquerda"
	self.printable2(tree.left)
	print "Direita"
	self.printable2(tree.right)
	print "FIM", tree.value

    def printable(self):
	#print "LOL"
	self.printable2(self)


def isPlain(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    return pos == LevelPositionTypes.plain.value;

def isHole(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    return pos == LevelPositionTypes.hole.value;

def isEnemy(pos):  
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    return pos == LevelPositionTypes.enemy.value;

def calculateFitness(tree):
    """
    Calculates the fitness of the tree (individual).

    :return: the calculated fitness
    """
	
    #Plain Values
    fitness = 0;
    positionReached = 0;
	
	#Tree Pointer
    root = tree;
	
	#Iterate on Level
    currentLevel = level;
	
    for step in currentLevel:
	
		#Reset Iteration
        currentTree = root;
		
		#Iterate on Nodes
	#print "---INICIO DA LOCURA DO RAFA"
	#print currentTree.value
	#print [n.value for n in Moves]
	#procurando um Terminal
	#currentTree.printable()
        while not currentTree.value in [n.value for n in Moves]:
		
            if (currentTree.value == LevelPositionTypes.plain.value):
                if isPlain(currentLevel[positionReached]):
		    #print "CT", currentTree.value, "L", currentTree.left
                    currentTree = currentTree.left;
                else:
                    currentTree = currentTree.right;
		    #print "CT", currentTree.value, "R", currentTree.right
            else:
                if (currentTree.value == LevelPositionTypes.hole.value):
                    if isHole(currentLevel[positionReached]):
			#print "CT", currentTree.value, "L", currentTree.left
                        currentTree = currentTree.left;
                    else:
			#print "CT", currentTree.value, "R", currentTree.right
                        currentTree = currentTree.right;
                else:
                    if (currentTree.value == LevelPositionTypes.enemy.value):
                        if isEnemy(currentLevel[positionReached]):
			    #print "CT", currentTree.value, "L", currentTree.right
                            currentTree = currentTree.left;
                        else:
			    #print "CT", currentTree.value, "R", currentTree.right
                            currentTree = currentTree.right;

	#print "---FIM DA LOCURA DO RAFA"
        #Certamente aqui tem um Terminals
        if (step == LevelPositionTypes.plain.value):
            if (currentTree.value == Moves.right or currentTree.value == Moves.jump):
                positionReached = positionReached + 1;
        else:
            if (step == LevelPositionTypes.hole.value):
                if (currentTree.value == Moves.jump):
                    positionReached = positionReached + 1;
                else:
                    if (currentTree.value == Moves.right):
                        break; #Dies
            else:
                if (step == LevelPositionTypes.enemy.value):
                    if (currentTree.value == Moves.jump):
                        positionReached = positionReached + 1;
                    else:
                        if (currentTree.value == Moves.fire):
                            currentLevel[positionReached] = LevelPositionTypes.plain.value;
                        else:
                            break; #Dies

    # Digite aqui sua funcao de fitness
    levelSize = len(level) - 1;
	
    fitness = (levelSize - positionReached + 1) * (levelSize) * (Tree.getTreeSize_rec(root));
	
    """
    RAFAEL: 
    Efeito: Maior peso e a posicao alcancada na fase pelo jogador, porem tambem leva em conta o tamanho do arvore de solucao
    Melhor Caso = Tamanho da Fase | Pior Caso = Tamanho da Fase2 * Tamanho da Arvore
    Melhor Fitness = Menor Fitness
    """

    return fitness;


