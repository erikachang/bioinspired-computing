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
	
class Tree(Enum):
    right = None  #False
    left = None	  #True
    value = None  #LevelPositionTypes(Node) OR Moves(Terminal)
    fitness = 0   #Fitness

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

def getTreeSize_rec(tree):
	
	if (type(currentTree) is Moves):
		return 1;
	
	left = 0;
	right = 0;
	
	if (tree.left != None):
		left = getTreeSize_rec(tree.left);
		
	if (tree.right != None):
		right = getTreeSize_rec(tree.right);

	return left + right + 1;
	
def getTreeSize(tree):
	"""
    Return size of the Tree
    """

	return getTreeSize_rec(tree);
	
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
        while type(currentTree) is not Moves:
		
            if (currentTree.value == LevelPositionTypes.plain):
                if isPlain(currentLevel[positionReached]):
                    currentTree = currentTree.left;
                else:
                    currentTree = currentTree.right;
            else:
                if (currentTree.value == LevelPositionTypes.hole):
                    if isHole(currentLevel[positionReached]):
                        currentTree = currentTree.left;
                    else:
                        currentTree = currentTree.right;
                else:
                    if (currentTree.value == LevelPositionTypes.enemy):
                        if isEnemy(currentLevel[positionReached]):
                            currentTree = currentTree.left;
                        else:
                            currentTree = currentTree.right;

        #Terminals
        if (step == LevelPositionTypes.plain):
            if (currentTree.value == Moves.right or currentTree.value == Moves.jump):
                positionReached = positionReached + 1;
        else:
            if (step == LevelPositionTypes.hole):
                if (currentTree.value == Moves.jump):
                    positionReached = positionReached + 1;
                else:
                    if (currentTree.value == Moves.right):
                        break; #Dies
            else:
                if (step == LevelPositionTypes.enemy):
                    if (currentTree.value == Moves.jump):
                        positionReached = positionReached + 1;
                    else:
                        if (currentTree.value == Moves.fire):
                            currentLevel[positionReached] = LevelPositionTypes.plain;
                        else:
                            break; #Dies

    # Digite aqui sua funcao de fitness
    levelSize = len(level) - 1;
	
    fitness = (levelSize - positionReached + 1) * (levelSize) * (getTreeSize(root));
	
    """
    RAFAEL: 
    Efeito: Maior peso e a posicao alcancada na fase pelo jogador, porem tambem leva em conta o tamanho do arvore de solucao
    Melhor Caso = Tamanho da Fase | Pior Caso = Tamanho da Fase2 * Tamanho da Arvore
    Melhor Fitness = Menor Fitness
    """

    return fitness;
