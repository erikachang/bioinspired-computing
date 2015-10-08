import fileParser
import networkx as nx
import random
import sys
import city
import operator
from sets import Set

ORIGIN_CITY = 0
DESTINATION_CITY = 1

class Aco():

    def __init__(self, alpha, beta, rho, k, iterations):
        self.cities = []
        self.connections = []
        self.G = nx.Graph()
        #Number of ants
        self.k = k
        #Number of rounds
        self.rounds = iterations
        self.alpha = alpha
        self.beta = beta
        self.p = rho
        self.Q = 10
        self.bestSolution= [[], float("inf")]
    
    def loadFile(self, f):
        self.cities, self.connections, self.G = fileParser.parseFile(f)

    def main(self, file):
        self.loadFile(file)
        self.executeAco()

    def executeAco(self):
        solution = []
        solutions = []
        for i in range(self.rounds):
            solutions = []
            costs = []
            for j in range(self.k):
                #set to the initial state
                currentCity = ORIGIN_CITY
                # operations of ant j
                solution = []
                cost = 0
                while currentCity != DESTINATION_CITY:
                    city = self.nextCity(j, currentCity)
                    solution.append(city)
                    currentCity = city.destination.cId
                    cost += city.size
                costs.append([solution, cost])         
                solutions.append(solution)
            # update best solution
            self.updateBestSolution(solutions, costs)
            # update pheromones trails
            self.updatePheromones(solutions, costs)
        print self.bestSolution

    def nextCity(self, ant, cIndex):
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

    def updateBestSolution(self, solutions, costs):
        sortedCosts = sorted(costs, key=operator.itemgetter(1))
        if sortedCosts[0][1] < self.bestSolution[1]:
            self.bestSolution = sortedCosts[0]

    """ Reduce every path ONLY ONE TIME using the evaporation coefficient (Rho -> self.p)
    We are also returning the cost of each solution here to improve performance
    NOT BEING USED
    """
    def updateRhoAndGetCost(self, solutions):
        alreadyUpdated = Set()
        costs = []
        for solution in solutions:
            cost = 0
            for connection in solution:
                if connection not in alreadyUpdated:
                    alreadyUpdated.add(connection)
                    connection.concentration = connection.concentration * (1-self.p)
                cost += connection.size
            costs.append(cost)
        return costs
    
    """ Update done in two steps: First we update the coefficient of evaporation of each connection, 
    then we compute how much pheromone was deposited in each connection
    """
    def updatePheromones(self, solutions, costs):
        count = 0
        for city in self.cities:
           for connection in city.connections:
               connection.concentration = connection.concentration * (1 - self.p)
        for solution in solutions:
            for connection in solution:
                connection.concentration += self.Q / costs[count][1]        
            count += 1

if __name__ == "__main__":
    try:
        file = sys.argv[1]
        alpha = float(sys.argv[2])
        beta = float(sys.argv[3])
        rho = float(sys.argv[4])
        k = int(sys.argv[5])
        iterations = int(sys.argv[6])
    except:
        print 'usage: aco.py <file_name> <pheromone weight: float> <heuristic weight: float> <pheromone evaporation: float> <number of ants: int> <iterations: int>'
        print 'example: aco.py setup.txt 0.5 0.5 0.5 10 1000'
        sys.exit(0)
        
    aco = Aco(alpha, beta, rho, k, iterations)
    aco.main(file)
