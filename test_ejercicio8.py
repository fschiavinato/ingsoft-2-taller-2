import unittest

from ejercicio8 import crossover


class TestCase(unittest.TestCase):
    def test1(self):
        # Test para cadenas cortas
        p = "aaaa"
        m = "bbbb"
        h1, h2 = crossover(p, m)
        flag = False
        for i in range(len(p)+1):
            for j in range(len(m)+1):
                flag = flag or ((h1[:i] == p[:i] and h1[i:] == m[j:]) and (h2[:j] == m[:j] and h2[j:] == p[i:]))
        self.assertEqual(flag, True)
