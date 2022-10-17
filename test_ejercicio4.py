import unittest
from ejercicio4 import get_fitness_cgi_decode


class TestCase(unittest.TestCase):
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

    def test_6(self):
        self._assert("%1+", 0.8333333333333334)

    def test_7(self):
        self._assert("%", 2.0)

    def test_8(self):
        self._assert("%1", 2.0)

    def test_9(self):
        self._assert("+", 3.5)

    def test_10(self):
        self._assert("+%1", 2.0)

    def _assert(self, s, e):
        self.assertAlmostEqual(get_fitness_cgi_decode(s), e)
