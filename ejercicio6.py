from typing import Dict, List
import unittest
import ejercicio4
import ejercicio2


def evaluate_population(population: List[str]) -> Dict[str, float]:
    fitness = {}
    for individual in population:
        ejercicio2.distances_true = {}
        ejercicio2.distances_false = {}
        fitness[individual] = ejercicio4.get_fitness_cgi_decode(individual)
    return fitness


class TestCase(unittest.TestCase):
    def test_1(self):
        self._fitness = evaluate_population(["%AA", "%AU", "%UU", "Hello+Reader", ""])
        self._assert("%AA", 0)
        self._assert("%AU", 0.9230769230769231)
        self._assert("%UU", 1.9230769230769231)
        self._assert("Hello+Reader", 2.9722222222222223)
        self._assert("", 4.5)

    def _assert(self, s, e):
        self.assertAlmostEqual(self._fitness[s], e)
