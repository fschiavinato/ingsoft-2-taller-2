import unittest

from ejercicio6 import evaluate_population


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
