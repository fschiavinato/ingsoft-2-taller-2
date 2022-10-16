import unittest

from ejercicio8 import crossover


class TestCase(unittest.TestCase):
    def test1(self):
        p = "aaaa"
        m = "bbbb"
        h1, h2 = crossover(p, m)
        self.assertEqual(len(h1), 4)
        self.assertEqual(len(h2), 4)
        for i in range(len(p)):
            if h1[i] == p[i]:
                self.assertEqual(h2[i], m[i])
            else:
                self.assertEqual(h1[i], m[i])
                self.assertEqual(h2[i], p[i])
