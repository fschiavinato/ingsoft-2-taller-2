import unittest
import ejercicio6
from ejercicio7 import selection


class TestCase(unittest.TestCase):
    def test_1(self):
        fitness = ejercicio6.evaluate_population(
            ["%AA", "%AU", "%UU", "Hello+Reader", ""]
        )
        best = selection(fitness, 1000)
        self.assertEqual(best, "%AA")
