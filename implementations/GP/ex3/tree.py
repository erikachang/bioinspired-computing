from utils import *

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
    
    def depth(self, tree):
        # return tree's depth

        if tree == None :
            return 0
            
        left = self.depth(tree.left) + 1

        right = self.depth(tree.right) + 1

        higher = left
        if higher < right :
            higher = right

        return higher
    
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