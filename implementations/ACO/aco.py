from fileParser import parse_file
import networkx as nx
import random
import sys
import operator
from solution import Solution
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
        self.best_solution = None

    def load_file(self, f):
        self.cities, self.connections, self.G = parse_file(f)

    def main(self, file):
        self.load_file(file)
        print '{0:.1f}|{1:.1f}|{2:.1f}|{3:d}|{4:d}'.format(self.alpha, self.beta, self.p, self.k, self.rounds)
        for i in range(10):
            self.execute_aco()

    def execute_aco(self):
        for i in range(self.rounds):
            solutions = []
            for j in range(self.k):
                # set to the initial state
                current_city = ORIGIN_CITY
                # operations of ant j
                solution = Solution()
                while current_city != DESTINATION_CITY:
                    city = self.next_city(j, current_city)
                    solution.add_city(city)
                    current_city = city.destination.cId
                solutions.append(solution)
            # update best solution
            self.update_best_solution(solutions)
            # update pheromones trails
            self.update_pheromones(solutions)
        print self.best_solution

    def next_city(self, ant, city_index):
        # index = random.randint(0, len(self.cities[state].connections) - 1)
        denominator = 0
        for connection in self.cities[city_index].connections:
            denominator += (connection.concentration ** self.alpha) * ((1 / connection.size) ** self.beta)

        probabilities = []
        for connection in self.cities[city_index].connections:
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
                return self.cities[city_index].connections[count]
            count += 1

    def update_best_solution(self, solutions):
        sorted_costs = sorted(solutions, key=operator.attrgetter('cost'))
        if self.best_solution is None or sorted_costs[0].cost < self.best_solution.cost:
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
    def update_pheromones(self, solutions):
        count = 0
        for city in self.cities:
            for connection in city.connections:
                connection.concentration *= (1 - self.p)
        for solution in solutions:
            for connection in solution.cities_traversed:
                connection.concentration += self.Q / solution.cost
        #Elitist ant system
        for connection in self.best_solution.cities_traversed:
             connection.concentration += self.Q / self.best_solution.cost


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
