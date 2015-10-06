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
        self.k = 10
        #Number of rounds
        self.rounds = 10
        self.alpha = 0.5
        self.beta = 0.5
    
    def loadFile(self, f):
        self.cities, self.connections, self.G = fileParser.parseFile(f)

    def main(self, file):
        self.loadFile(file)
        self.executeAco()

    def executeAco(self):
        solution = []
        solutions = []
        for i in range(self.rounds):
            for j in range(self.k):
                #set to the initial state
                currentState = ORIGIN_CITY
                # operations of ant j
                solution = []
                while currentState != DESTINATION_CITY:
                    action = self.getAction(j, currentState)
                    solution.append(action)
                    currentState = action.destination.cId
                #calculate pheronome distribution
                
                solutions.append(solution)
            print solution

            # evaluate the cost of every solution built
            
            # update best solution

            # update pheromones trails

    def getAction(self, ant, cIndex):
        # index = random.randint(0, len(self.cities[state].connections) - 1)
        denominator = 0
        for connection in self.cities[cIndex].connections:
            denominator += (connection.concentration ** self.alpha) *  ((1 / connection.size) ** self.beta)

        probabilities = []
        for connection in self.cities[cIndex].connections:
            p = ((connection.concentration ** self.alpha) *  ((1 / connection.size) ** self.beta)) / denominator
            probabilities.append(p)

        ranges = []
        boundary = 0
        for probability in probabilities:
            boundary += probability * 100
            ranges.append(boundary)

        selection = random.randint(0, 99)

        count = 0
        for range in ranges:
            if selection < range:
                return self.cities[cIndex].connections[count]
            count += 1
            


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except:
        print 'usage: aco.py <file_name>'
        sys.exit(0)
    aco = Aco()
    aco.main(file)
