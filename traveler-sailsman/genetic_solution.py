import numpy as np
import copy as cp


# cities:
cities = ['a', 'b', 'c', 'd']
# routes:
routes = ['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']
# costs:
costs = np.random.randint(1, 11, 12)


class Chromosome:
    def __init__(self, coding, adap_level=0):
        self.coding = coding
        self.adap = adap_level

    def __str__(self):
        return "Coding: {}\nAdaptation level: {}\n".format(self.coding, self.adap)


def print_population(population):
    for a in population:
        print(a)


def adap_calc(pop):
    # calculating the adaptation
    for i in range(len(pop)):
        # streets of a chromosome (a solution)
        streets = []
        for j in range(12):
            if pop[i].coding[j] == 1:
                streets.append(j)
        # making the calculation of the adaptation level
        for street in streets:
            pop[i].adap -= costs[street]
        # looking for impossible solutions
        for town in cities:
            times = 0
            for street in streets:
                if town in routes[street]:
                    times += 1
            if times != 2:
                # highest penalty
                pop[i].adap = -999
    return pop


def main():
    # initial population (10 individuals)
    pop = []
    for p in range(10):
        pop.append(Chromosome(np.random.randint(0, 2, 12)))
    # 100 generations:
    for gen in range(100):
        pop = adap_calc(pop)

        # making the selection
        pop.sort(key=lambda x: x.adap, reverse=True)

        old_pop = cp.deepcopy(pop[5:])
        pop = cp.deepcopy(pop[:5])

        # making the cross
        descendants = []
        for i in range(5):
            for j in range(5):
                # 40%
                if np.random.randint(0, 101) > 60:
                    x = np.random.randint(0, 12)
                    aux = np.zeros(12)
                    aux[:x] = cp.deepcopy(pop[i].coding[:x])
                    aux[x:] = cp.deepcopy(old_pop[j].coding[x:])
                    descendants.append(Chromosome(aux))

        descendants += cp.deepcopy(old_pop)

        # mutation
        for i in range(len(descendants)):
            # 10%
            if np.random.randint(0, 101) > 90:
                x = np.random.randint(0, 12)
                if descendants[i].coding[x] == 0:
                    descendants[i].coding[x] = 1
                else:
                    descendants[i].coding[x] = 0

        descendants = adap_calc(descendants)
        descendants.sort(key=lambda x: x.adap, reverse=True)

        # replacement
        j = 0  # pop
        k = 0  # descendants
        pop_aux = []
        for i in range(11):
            if j < len(pop) and k < len(descendants):
                if pop[j].adap >= descendants[k].adap:
                    pop_aux.append(cp.deepcopy(pop[j]))
                    j += 1
                else:
                    pop_aux.append(cp.deepcopy(descendants[k]))
                    k += 1
            elif j < len(pop):
                pop_aux.append(cp.deepcopy(pop[j]))
                j += 1
            else:
                pop_aux.append(cp.deepcopy(descendants[k]))
                k += 1
        pop = pop_aux

    print_population(pop)


if __name__ == '__main__':
    main()
