import random
from subprocess import call
from traffic_light import Traffic_light

MAX_ITERATIONS = 10

class Pso:

    def __init__(self, population_size=60, traffic_lights=5, n_cars=450, n_iterations=60, seed=2): 
        
        self.population_size = population_size
        self.traffic_lights  = traffic_lights
        self.global_best     = 0
        self.population      = []
        self.n_cars          = n_cars
        self.n_iterations    = n_iterations
        self.seed            = seed
        random.seed(self.seed)

    def create_population(self):
        # Create a population of traffic light configurations.

        max_time = random.randint(10, 50)
        max_vel  = random.randint(20, 40)
        min_vel  = random.randint(-40, -20)

        for individual in range(self.population_size):
           
            x = []      # List with times for a configuration.
            v = []      # List with velocities for each configuration

            for i in range(self.traffic_lights):
                # Start individual positions (traffic light times) radomly.
                x.append(random.randint(1, max_time))
                v.append(random.randint(min_vel, max_vel))

            self.population.append(Traffic_light(x, v))

    def write_input_param(self):

        input_file = open("entrada/input_params.txt", 'w')

        iterations = str(self.n_iterations) + "// iteracoes"

        cars       = str(self.n_cars) + "// carros"

        seed       = str(self.seed) + "// seed"

        input_file.write(iterations + "\n" + cars + "\n" + seed)

        input_file.close()


    def execute_POS(self):
        
        self.create_population()

        self.write_input_param()

        total_iterations = 0

        p_best = [0, 0]

        best_result = None

        while total_iterations < MAX_ITERATIONS and best_result < 3:

            print "Iteration: ", total_iterations + 1

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
                
                # Update velocities
                omega = random.randint(0, 1)

                phi_1 = [random.randint(0, 1) for i in range(self.traffic_lights)]
                phi_2 = [random.randint(0, 1) for i in range(self.traffic_lights)]

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


                for i in range(self.traffic_lights):
                    # Update individual's position
                    result = int(abs(individual.x[i] + individual.v[i]))
                    if not result:
                        # If the value is equal 0, we add 1.
                        individual.x[i] = result + 1
                    else:
                        individual.x[i] = result

            total_iterations += 1

        self.write_solution(self.population[self.global_best])
        call(["java", "-jar", "SwarmOptimization_2.jar", "entrada/" ])
        
        for sent in self.get_result():
            print sent
            
        return self.population[self.global_best]

    def calculate_fitness(self, individual):
        # Return the fitness of the individual applied to the scenario.

        self.write_solution(individual)
        self.execute_swarm()
        output = self.get_result()
        cars = output[0].split()[0]
        iterations = output[1].split()[0]

        return (int(iterations) + 1)/ float(int(cars) + 1)

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

    def get_result(self):

        input_file = open("entrada/output_params.txt")
        output = input_file.readlines()
        input_file.close()

        return output


if __name__ == "__main__":
    pso = Pso()
    best_solution = pso.execute_POS()