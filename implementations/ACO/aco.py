import fileParser
import networkx as nx
import random
import sys

ORIGIN_CITY = 0
DESTINATION_CITY = 1

class Aco():

    def __init__(self):
        self.cities = []
        self.connections = []
        self.G = nx.Graph()
        #Number of ants
        self.k = 1
        #Number of rounds
        self.rounds = 1
    
    def loadFile(self, f):
        self.cities, self.connections, self.G = fileParser.parseFile(f)

    def main(self, file):
        self.loadFile(file)
        self.executeAco()

    def executeAco(self):
        edgesVisited = []
        antEdgeList = []
        for i in range(self.rounds):
            for j in range(self.k):
                #set to the initial state
                currentState = ORIGIN_CITY
                # operations of ant j
                edgesVisited = []
                while currentState != DESTINATION_CITY:
                    action = self.getAction(j, currentState)
                    edgesVisited.append(action)
                    currentState = action.b.cId
                #calculate pheronome distribution
                antEdgeList.append(edgesVisited)
                print edgesVisited

    def getAction(self, ant, state):
        index = random.randint(0, len(self.cities[state].connections) - 1)
        return self.cities[state].connections[index]

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except:
        print 'usage: aco.py <file_name>'
        sys.exit(0)
    aco = Aco()
    aco.main(file)
