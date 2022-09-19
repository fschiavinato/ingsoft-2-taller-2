from typing import Dict, List
import ejercicio4
import ejercicio2


def evaluate_population(population: List[str]) -> Dict[str, float]:
    fitness = {}
    for individual in population:
        ejercicio2.distances_true = {}
        ejercicio2.distances_false = {}
        fitness[individual] = ejercicio4.get_fitness_cgi_decode(individual)
    return fitness


