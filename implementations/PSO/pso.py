import random
from traffic_light import Traffic_light

class Pso:

    def __init__(self, population_size, traffic_lights):
        
        self.population_size = population_size
        self. traffic_lights  = traffic_lights
        self.global_best     = -1
        self.population      = []

    def create_population(self):
        # Create a population of traffic light configurations.

        for individual in range(self.population_size):
            
            x = []      # List with times for a configuration.
            v = []      # List with velocities for each configuration
            
            for light in range(self.traffic_lights):
                # Start individual positions (traffic light times) radomly.

                x.append(random.randint(1, 100))
                v.append(random.randint(-30, 50))

            self.population.append(Traffic_light(x, v))

    def execute_POS(self):
        
        self.create_population()

        while self.global_best < 100:    

            for individual in self.population:
                # Given the fitness, update p_best, p, and global_best.

                fitness = self.calculate_fitness(individual)

                if fitness > individual.p_best:
                    individual.p_best = fitness
                    individual.p      = individual.x

                if individual.p_best > self.global_best:
                    self.global_best = individual.x
            
            for individual in self.population:
                # Update velocities and times of traffic lights.

                omega = random.randint(5, 10) / float(10)

                phi_1 = float("{0:.2f}".format(random.random()))
                phi_2 = float("{0:.2f}".format(random.random()))

                diff_p_x = [individual.p[i] - individual.x[i] for i in range(self.traffic_lights)]
                diff_global_x = [self.global_best[i] - individual.x[i] for i in range(self.traffic_lights)]

                mult_phi_1 = [element * phi_1 for element in diff_p_x]
                mult_phi_2 = [element * phi_2 for element in diff_global_x]
                mult_omega = [element * omega for element in individual.v]

                individual.v = [individual.v[i] + mult_phi_1[i] + mult_phi_2[i] for i in range(self.traffic_lights)]

                individual.x = [individual.x[i] + individual.v[i] for i in range(self.traffic_lights)]

        return self.population

    def calculate_fitness(self, individual):
        return random.randint(1, 40)

if __name__ == "__main__":
    pso = Pso(20, 5)
    population = pso.execute_POS()