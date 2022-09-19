import random
from typing import Tuple
import unittest


def crossover(parent1: str, parent2: str) -> Tuple[str, str]:
    l = min(len(parent1), len(parent2))
    i = random.randint(0, l)
    offspring1 = parent1[:i] + parent2[i:]
    offspring2 = parent2[:i] + parent1[i:]
    return offspring1, offspring2


class TestCase(unittest.TestCase):
    def test1(self):
        p = "aaaa"
        m = "bbbb"
        h1, h2 = crossover(p, m)
        self.assertEqual(len(h1), 4)
        self.assertEqual(len(h2), 4)
