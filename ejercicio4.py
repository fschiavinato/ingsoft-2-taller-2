import unittest
from ejercicio3 import cgi_decoded_instrumented
import ejercicio2


def get_fitness_cgi_decode(s: str) -> float:
    try:
        cgi_decoded_instrumented(s)
    except:
        pass
    max_branch = max(ejercicio2.distances_true.keys())
    approach_level = 5 - max_branch
    if max_branch == 2:
        branch_distance = ejercicio2.distances_false[max_branch]
    else:
        branch_distance = ejercicio2.distances_true[max_branch]

    normalized_branch_distance = branch_distance / (branch_distance + 1)

    return approach_level + normalized_branch_distance


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        ejercicio2.distances_true = {}
        ejercicio2.distances_false = {}
        return super().setUp()

    def test_1(self):
        self._assert("%AA", 0)

    def test_2(self):
        self._assert("%AU", 0.9230769230769231)

    def test_3(self):
        self._assert("%UU", 1.9230769230769231)

    def test_4(self):
        self._assert("Hello+Reader", 2.9722222222222223)

    def test_5(self):
        self._assert("", 4.5)

    def _assert(self, s, e):
        self.assertAlmostEqual(get_fitness_cgi_decode(s), e)
