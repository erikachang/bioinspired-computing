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
    __Right = None      #False
    __Left = None	#True
    __value = None	#LevelPositionTypes(Node) OR Moves(Terminal)

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
    fitness = 0;

    for step in level:
	print "TO DO - Function Fitness"

        # Digite aqui sua funcao de fitness
	"""
	RAFAEL: 
	Calculo: (Posicao do Player ate o Final da Fase + 1) * (Tamanho da Fase) * (Tamanho do Arvore)
	Efeito: Maior peso e a posicao alcancada na fase pelo jogador, porem tambem leva em conta o tamanho do arvore de solucao
	Melhor Caso = Tamanho da Fase | Pior Caso = Tamanho da Fase2 * Tamanho da Arvore
	Melhor Fitness = Menor Fitness
	"""

    return fitness;


