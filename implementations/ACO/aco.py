from fileParser import parseFile
import networkx as nx
import random
import sys
import operator
from sets import Set

ORIGIN_CITY = 0
DESTINATION_CITY = 1


class Aco:
    def __init__(self, alpha, beta, rho, k, iterations):
        self.cities = []
        self.connections = []
        self.G = nx.Graph()
        # Number of ants
        self.k = k
        # Number of rounds
        self.rounds = iterations
        self.alpha = alpha
        self.beta = beta
        self.p = rho
        self.Q = 10
        self.best_solution = [[], float("inf")]

    def load_file(self, f):
        self.cities, self.connections, self.G = parseFile(f)

    def main(self, file):
        self.load_file(file)
        self.execute_aco()

    def execute_aco(self):
        for i in range(self.rounds):
            solutions = []
            costs = []
            for j in range(self.k):
                # set to the initial state
                current_city = ORIGIN_CITY
                # operations of ant j
                solution = []
                cost = 0
                while current_city != DESTINATION_CITY:
                    city = self.next_city(j, current_city)
                    solution.append(city)
                    current_city = city.destination.cId
                    cost += city.size
                costs.append([solution, cost])
                solutions.append(solution)
            # update best solution
            self.update_best_solution(solutions, costs)
            # update pheromones trails
            self.update_pheromones(solutions, costs)
        print self.best_solution

    def next_city(self, ant, cityId):
        # index = random.randint(0, len(self.cities[state].connections) - 1)
        denominator = 0
        for connection in self.cities[cityId].connections:
            denominator += (connection.concentration ** self.alpha) * ((1 / connection.size) ** self.beta)

        probabilities = []
        for connection in self.cities[cityId].connections:
            p = ((connection.concentration ** self.alpha) * ((1 / connection.size) ** self.beta)) / denominator
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
                return self.cities[cityId].connections[count]
            count += 1

    def update_best_solution(self, solutions, costs):
        sorted_costs = sorted(costs, key=operator.itemgetter(1))
        if sorted_costs[0][1] < self.best_solution[1]:
            self.best_solution = sorted_costs[0]

    """ Reduce every path ONLY ONE TIME using the evaporation coefficient (Rho -> self.p)
    We are also returning the cost of each solution here to improve performance
    NOT BEING USED
    """

    def update_rho_and_get_cost(self, solutions):
        already_updated = Set() # SC@LA: I've just found out the sets package is deprecated
        costs = []
        for solution in solutions:
            cost = 0
            for connection in solution:
                if connection not in already_updated:
                    already_updated.add(connection)
                    connection.concentration *= (1 - self.p)
                cost += connection.size
            costs.append(cost)
        return costs

    """ Update done in two steps: First we update the coefficient of evaporation of each connection, 
    then we compute how much pheromone was deposited in each connection
    """
    def update_pheromones(self, solutions, costs):
        count = 0
        for city in self.cities:
            for connection in city.connections:
                connection.concentration *= (1 - self.p)
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
    except IndexError:
        print 'usage: aco.py {0:s} {1:s} {2:s} {3:s} {4:s} {5:s}'.format('<file_name>',
                                                                         '<pheromone weight: float>',
                                                                         '<heuristic weight: float>',
                                                                         '<pheromone evaporation: float>',
                                                                         '<number of ants: int>',
                                                                         '<iterations: int>')
        print 'example: aco.py setup.txt 0.5 0.5 0.5 10 1000'
        sys.exit(0)

    aco = Aco(alpha, beta, rho, k, iterations)
    aco.main(file)
