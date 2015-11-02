import copy
import random
from subprocess import call
from traffic_light import Traffic_light

MAX_ITERATIONS = 500

class Pso:

    def __init__(self, population_size=100, traffic_lights=5, n_cars=300, n_iterations=60, seed=1):
        
        self.population_size = population_size
        self.traffic_lights  = traffic_lights
        self.global_best     = 0
        self.population      = []
        self.n_cars          = n_cars
        self.n_iterations    = n_iterations
        random.seed(seed)

    def create_population(self):
        # Create a population of traffic light configurations.

        for individual in range(self.population_size):
            
            x = []      # List with times for a configuration.
            v = []      # List with velocities for each configuration
            
            for i in range(self.traffic_lights):
                # Start individual positions (traffic light times) radomly.
                x.append(random.randint(1, 70))
                v.append(random.randint(-40, 40))

            self.population.append(Traffic_light(x, v))

    def execute_POS(self):
        
        self.create_population()

        total_iterations = 0

        p_best = [0, 0]

        while total_iterations < MAX_ITERATIONS:

            for individual in self.population:
                # Given the fitness, update p_best, p, and global_best.

                fitness = self.calculate_fitness(individual)

                if fitness > individual.p_best:
                    individual.p_best = fitness
                    individual.p      = individual.x

                if individual.p_best > p_best[0]:
                    # Get the higher p_best among all individuals.
                    p_best[0] = individual.p_best
                    p_best[1] = self.population.index(individual)
            
            self.global_best = p_best[1] 
            
            for individual in self.population:
                # Update velocities and times of traffic lights.

                omega = random.randint(5, 10) / float(10)

                phi_1 = [random.randint(1, 10) / float(10) for i in range(self.traffic_lights)]
                phi_2 = [random.randint(1, 10) / float(10) for i in range(self.traffic_lights)]

                diff_p_x = [
                                individual.p[i] - individual.x[i]
                                for i in range(self.traffic_lights)
                           ]    # (p_i - x_i)

                diff_global_x = [
                                    self.population[self.global_best].x[i] - individual.x[i]
                                    for i in range(self.traffic_lights)
                                ]   # (p_best_global - x_i)

                mult_phi_1 = [
                                diff_p_x[i] * phi_1[i]
                                for i in range(self.traffic_lights)
                             ]  # (U_phi_1 * diff_p_x)

                mult_phi_2 = [
                                diff_global_x[i] * phi_2[i]
                                for i in range(self.traffic_lights)
                             ]  # (U_phi_2 * diff_global_x)

                mult_omega = [
                                element * omega
                                for element in individual.v
                            ]   # omega * current_velocity

                individual.v = [
                                    mult_omega[i] + mult_phi_1[i] + mult_phi_2[i]
                                    for i in range(self.traffic_lights)
                               ]    # Update individual velocity.

                # print self.population.index(individual), individual.v

                individual.x = [
                                    int(individual.x[i] + individual.v[i]) + 1
                                    for i in range(self.traffic_lights)
                               ]

                # print self.population.index(individual), individual.x

            total_iterations += 1

        self.write_solution(self.population[self.global_best])
        self.execute_swarm()
        self.print_result()
            
        return self.population[self.global_best]

    def calculate_fitness(self, individual):
        # Return the fitness of the individual applied to the scenario.

        car_for_traffic_light = []

        copy_individual = copy.deepcopy(individual)

        cars = self.n_cars      # Total number of cars;
        iterations = self.n_iterations

        for i in range(self.traffic_lights):
            # Divide cars between each traffic light.
            if i == 0:
                car_for_traffic_light.append(0)
            else:
                car_for_traffic_light.append(self.n_cars / self.traffic_lights)

        while iterations > 0 and cars > 0:
            """
                Simulate the traffic lights.
                Each iteration is an unity of time for the traffic lights.
                We start by the combination down, left, right.
            """

            # First intersaction.

            if copy_individual.x[0] > 0:   
                # Traffic light down.             
                if car_for_traffic_light[0] > 0:
                    car_for_traffic_light[0] -= 5   # Each iteration frees five cars.
                    cars -= 5
                copy_individual.x[0] -= 1           # Decrease time for the current traffic light.

            elif copy_individual.x[1] > 0:
                if car_for_traffic_light[1] > 0:
                    car_for_traffic_light[1] -= 5
                    cars -= 5
                copy_individual.x[1] -= 1

            elif copy_individual.x[2] > 0:
                if car_for_traffic_light[2] > 0:
                    car_for_traffic_light[2] -= 5
                    cars -= 5
                copy_individual.x[2] -= 1
                if copy_individual.x[2] == 0:
                    copy_individual.x[0] = individual.x[0]
                    copy_individual.x[1] = individual.x[1]
                    copy_individual.x[2] = individual.x[2]

            # Second intersection.

            if copy_individual.x[3] > 0:
                # Traffic light down.
                if car_for_traffic_light[3] > 0:
                    car_for_traffic_light[3] -= 5   # Decrease the number of cars in the current traffic light.
                    car_for_traffic_light[0] += 5   # Increase the number of cars in down 
                copy_individual.x[3] -= 1

            elif copy_individual.x[4] > 0:
                # Traffic light left.
                if car_for_traffic_light[4] > 0:
                    car_for_traffic_light[4] -= 5
                    car_for_traffic_light[0] += 5
                copy_individual.x[4] -= 1
                if copy_individual.x[4] == 0:
                    copy_individual.x[3] = individual.x[3]
                    copy_individual.x[4] = individual.x[4]

            iterations -= 1

        return (iterations + 1)/ float(cars + 1)

    def write_solution(self, best_solution):
        # Get the best individual and write on times file.

        output_file = open("entrada/times.txt", 'w')

        for i in range(len(best_solution.x)):
            if i < 2:
                output_file.write(str(best_solution.x[i]) + ",")
            elif i == 2:
                output_file.write(str(best_solution.x[i]))
            elif i == 3:
                output_file.write("\n" + str(best_solution.x[i]) + ",")
            else:
                output_file.write(str(best_solution.x[i]))

        output_file.close()

    def execute_swarm(self):
        # Execute Java simulation.

        call(["java", "-jar", "SwarmOptimization.jar", "entrada/" ])

    def print_result(self):

        input_file = open("entrada/output_params.txt")
        output = input_file.read()

        print output

        input_file.close()    

if __name__ == "__main__":
    pso = Pso()
    best_solution = pso.execute_POS()