"""utils.py

This file stands for helper functions to be used
when evaluating the level vector.
"""

from enum import Enum
import sys
import copy

level = ['P','P','P','H','H','P','P','P','H','P','P','P','P','H','P','P','E','E','P','P']    

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

    
    def getTreeSize(tree):        
        # return the size of the tree

        # if it is a terminal return 1
        if (tree.value in [n.value for n in Moves]):
            return 1
        
        left = 0
        right = 0
        
        # iterate recursively through the tree
        if (tree.left != None):
            left = Tree.getTreeSize(tree.left)
            
        if (tree.right != None):
            right = Tree.getTreeSize(tree.right)

        return left + right + 1
    
    def printTree2(self, tree):
        # print the tree elements recursively
        if tree == None:
            return 0

        print tree.value

        print "Left branch"
        self.printTree2(tree.left)
        print "Right branch"
        self.printTree2(tree.right)
        print "End branch", tree.value

    def printTree(self):
        self.printTree2(self)


def isPlain(pos):
    """
    Verifies if the given position is a plain.
    :param pos: the level vector position
    :return: True if it's a plain. False otherwise.
    """
    return pos == LevelPositionTypes.plain.value

def isHole(pos):
    """
    Verifies if the given position is a hole.
    :param pos: the level vector position
    :return: True if it's a hole. False otherwise.
    """
    return pos == LevelPositionTypes.hole.value

def isEnemy(pos):  
    """
    Verifies if the given position is a enemy.
    :param pos: the level vector position
    :return: True if it's a enemy. False otherwise.
    """
    return pos == LevelPositionTypes.enemy.value

def calculateFitness(tree):
    """
    Calculates the fitness of the tree (individual).

    :return: the calculated fitness
    """
    
    # Plain Values
    fitness = 0
    positionReached = 0
    
    # Tree Pointer
    root = tree
    
    # Iterate on Level
    currentLevel = copy.deepcopy(level)
    for step in range(len(currentLevel)):
    
        # Reset Iteration
        currentTree = root
        
        # Iterate on Nodes
        while not currentTree.value in [n.value for n in Moves]:
        
            if (currentTree.value == LevelPositionTypes.plain.value):
                if isPlain(currentLevel[positionReached]):
                    currentTree = currentTree.left
                else:
                    currentTree = currentTree.right
            elif (currentTree.value == LevelPositionTypes.hole.value):
                if isHole(currentLevel[positionReached]):
                    currentTree = currentTree.left
                else:
                    currentTree = currentTree.right
            elif (currentTree.value == LevelPositionTypes.enemy.value):
                if isEnemy(currentLevel[positionReached]):
                    currentTree = currentTree.left
                else:
                    currentTree = currentTree.right

            # Terminals
            if (currentLevel[step] == LevelPositionTypes.plain.value):
                if (currentTree.value == Moves.right.value or currentTree.value == Moves.jump.value):
                    positionReached = positionReached + 1
            elif (currentLevel[step] == LevelPositionTypes.hole.value):
                if (currentTree.value == Moves.jump.value):
                    positionReached = positionReached + 1
                elif (currentTree.value == Moves.right.value):
                    break # Dies
            elif (currentLevel[step] == LevelPositionTypes.enemy.value):
                if (currentTree.value == Moves.jump.value):
                    positionReached = positionReached + 1
                elif (currentTree.value == Moves.fire.value):
                    currentLevel[step] = LevelPositionTypes.plain.value
                else:
                    break #Dies

    levelSize = len(level)
    treeSize = Tree.getTreeSize(root)

    # calculate fitness by subtracting the position reached by the tree by the level size
    # sum this with the size of the tree divided by 100
    # a tree that reached the intire level will return a lower fitness
    fitness = float(levelSize - positionReached) + (float(treeSize) / float(100))
    
    return fitness


