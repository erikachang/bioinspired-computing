
class Solution:
    def __init__(self):
        self.cities_traversed = []
        self.cost = 0

    def add_city(self, city):
        self.cities_traversed.append(city)
        self.cost += city.size

    def __repr__(self):
        solution_str = str(self.cities_traversed[0].origin.cId)
        for city in self.cities_traversed:
            solution_str += '|' + str(city.destination.cId)
        return solution_str
