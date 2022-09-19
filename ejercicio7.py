import random
from typing import Dict
import ejercicio6
import unittest

def selection(evaluated_population: Dict[str, float], tournament_size):
    tournament = random.choices(list(evaluated_population.keys()), k=tournament_size)
    max_fitness = min(evaluated_population[player] for player in tournament)
    return next(player for player in tournament if evaluated_population[player] == max_fitness)

class TestCase(unittest.TestCase):

    def test_1(self):
        fitness = ejercicio6.evaluate_population(["%AA", "%AU", "%UU", "Hello+Reader", ""])
        best = selection(fitness, 1000)
        self.assertEquals(best, "%AA")
