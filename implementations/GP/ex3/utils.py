"""utils.py

This file stands for helper functions to be used
when evaluating the level vector.
"""

from enum import Enum
import random
import sys
from tree import *

base_level = ['P','P','P','H','P','P','H','P','P','E','P','P','P','H','H','P','H','H','P','P','E','P','E','P','E','H','H','P','P','E','P','H','H','P','P']
level = []

class LevelPositionTypes(Enum):
    plain = 'P'
    hole = 'H'
    enemy = 'E'

class Node(Enum):
	plain1right = "P1R"
	plain2right = "P2R"
	plain1left = "P1L"
	plain2left = "P1L"
	hole1right = "H1R"
	hole2right = "H2R"
	hole1left = "H1L"
	hole2left = "H2L"
	enemy1right = "E1R"
	enemy2right = "E2R"
	enemy1left = "E1L"
	enemy2left = "E2L"
	
class Moves(Enum):
    jump_right = "R_J"
    jump_run_right = "RQJ"
    right = "R__"
    run_right = "RQ_"
    jump_left = "L_J"
    jump_run_left = "LQJ"
    left = "L__"
    run_left = "LQ_"


def isHole1StepsRight(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    if (pos + 1) >= len(level): return False
    return level[pos + 1] == LevelPositionTypes.hole.value


def isHole2StepsRight(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    if (pos + 2) >= len(level): return False
    return level[pos + 2] == LevelPositionTypes.hole.value

def isHole1StepsLeft(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    if (pos - 1) < 0: return False
    return level[pos - 1] == LevelPositionTypes.hole.value


def isHole2StepsLeft(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    if (pos - 2) < 0: return False
    return level[pos - 2] == LevelPositionTypes.hole.value


def isEnemy1StepsRight(pos):
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    if (pos + 1) >= len(level): return False
    return level[pos + 1] == LevelPositionTypes.enemy.value


def isEnemy2StepsRight(pos):
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    if (pos + 2) >= len(level): return False
    return level[pos + 2] == LevelPositionTypes.enemy.value

def isEnemy1StepsLeft(pos):
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    if (pos - 1) < 0: return False
    return level[pos - 1] == LevelPositionTypes.enemy.value


def isEnemy2StepsLeft(pos):
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    if (pos - 2) < 0: return False
    return level[pos - 2] == LevelPositionTypes.enemy.value

def isPlain1StepsRight(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    if (pos + 1) >= len(level): return False
    return level[pos + 1] == LevelPositionTypes.plain.value


def isPlain2StepsRight(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    if (pos + 2) >= len(level): return False
    return level[pos + 2] == LevelPositionTypes.plain.value

def isPlain1StepsLeft(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    if (pos - 1) < 0: return False
    return level[pos - 1] == LevelPositionTypes.plain.value


def isPlain2StepsLeft(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    if (pos - 2) < 0: return False
    return level[pos - 2] == LevelPositionTypes.plain.value

def evaluateTree(tree, position):
	# return tree at position

    levelType = level[position]
    currentTree = tree
    
    # iterate on nodes
    while not currentTree.value in [n.value for n in Moves]:
        if (currentTree.value == Node.plain1right.value):
            if(isPlain1StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.plain2right.value):
            if(isPlain2StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.plain1left.value):
            if(isPlain1StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.plain2left.value):
            if(isPlain2StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.hole1right.value):
            if(isHole1StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.hole2right.value):
            if(isHole2StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.hole1left.value):
            if(isHole1StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.hole2left.value):
            if(isHole2StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.enemy1right.value):
            if(isEnemy1StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.enemy2right.value):
            if(isEnemy2StepsRight(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.enemy1left.value):
            if(isEnemy1StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
        elif (currentTree.value == Node.enemy2left.value):
            if(isEnemy2StepsLeft(position)):
                currentTree = currentTree.left
            else:
                currentTree = currentTree.right
	
	return currentTree.value
	
def calculateFitness(tree):
    """
    Calculates the fitness of the tree (individual).

    :return: the calculated fitness
    """

    fitness = 0
    state = 0 # Start with small size
    position = 0 # Start position
    stepCounter = 0

    global level
    level = list(base_level)


    while(position < len(level) and stepCounter < 80):
    	
        calculatedStep = evaluateTree(tree, position)

        # Enemy walk random
        for i in range(len(level)):
                if level[i] == LevelPositionTypes.enemy.value:
                        rand = random.randint(0,2)
                        if level[i + rand - 1] == LevelPositionTypes.plain.value:
                                level[i + rand - 1] = LevelPositionTypes.enemy.value
                                level[i] = LevelPositionTypes.plain.value

        steps = 0
        direction = 0

        if "R" in calculatedStep:
                direction = 1
        else:
                direction = -1

        if "Q" in calculatedStep:
                steps = 3
        else:
                steps = 2

        for i in range(steps):

                position += direction

                if position < 0:
                        position = 0
                        break

                if position >= len(level):
                        break

                if level[position] in (LevelPositionTypes.enemy.value, LevelPositionTypes.hole.value) and "J" not in calculatedStep :
                        fitness = fitness - 10 # Mario morreu
                        stepCounter = 100

        if position >= len(level):
                fitness += (80 - stepCounter)/2 # Mario passou de fase
                break

        if  "J" in calculatedStep and level[position] == LevelPositionTypes.enemy.value:
                fitness = fitness + 2 # Mario kills an enemy
                level[position] = "P"

        if level[position] == LevelPositionTypes.hole.value:
                fitness = fitness - 10 # Mario morreu
                stepCounter = 100


        stepCounter += 1

    fitness += position

    fitness = fitness - tree.depth(tree)/2

    if stepCounter > 100:
            fitness -= 8

    return fitness


