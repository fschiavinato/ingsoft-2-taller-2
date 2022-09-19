import unittest
import sys

from ejercicio2 import evaluate_condition
import ejercicio2


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(evaluate_condition(0, "Eq", 20, 10), False)
        self.assertEqual(ejercicio2.distances_true[0], 10)
        self.assertEqual(ejercicio2.distances_false[0], 0)

    def test_2(self):
        self.assertEqual(evaluate_condition(1, "Eq", 20, 20), True)
        self.assertEqual(ejercicio2.distances_true[1], 0)
        self.assertEqual(ejercicio2.distances_false[1], 1)

    def test_3(self):
        self.assertEqual(evaluate_condition(2, "Ne", 20, 10), True)
        self.assertEqual(ejercicio2.distances_true[2], 0)
        self.assertEqual(ejercicio2.distances_false[2], 10)

    def test_4(self):
        self.assertEqual(evaluate_condition(3, "Ne", 20, 20), False)
        self.assertEqual(ejercicio2.distances_true[3], 1)
        self.assertEqual(ejercicio2.distances_false[3], 0)

    def test_5(self):
        self.assertEqual(evaluate_condition(4, "Le", 10, 20), True)
        self.assertEqual(ejercicio2.distances_true[4], 0)
        self.assertEqual(ejercicio2.distances_false[4], 11)

    def test_6(self):
        self.assertEqual(evaluate_condition(5, "Le", 20, 10), False)
        self.assertEqual(ejercicio2.distances_true[5], 10)
        self.assertEqual(ejercicio2.distances_false[5], 0)

    def test_7(self):
        self.assertEqual(evaluate_condition(6, "Le", 20, 20), True)
        self.assertEqual(ejercicio2.distances_true[6], 0)
        self.assertEqual(ejercicio2.distances_false[6], 1)

    def test_8(self):
        self.assertEqual(evaluate_condition(7, "Lt", 10, 20), True)
        self.assertEqual(ejercicio2.distances_true[7], 0)
        self.assertEqual(ejercicio2.distances_false[7], 10)

    def test_9(self):
        self.assertEqual(evaluate_condition(8, "Lt", 20, 10), False)
        self.assertEqual(ejercicio2.distances_true[8], 11)
        self.assertEqual(ejercicio2.distances_false[8], 0)

    def test_10(self):
        self.assertEqual(evaluate_condition(9, "Lt", 20, 20), False)
        self.assertEqual(ejercicio2.distances_true[9], 1)
        self.assertEqual(ejercicio2.distances_false[9], 0)

    def test_11(self):
        self.assertEqual(evaluate_condition(10, "In", 10, []), False)
        self.assertEqual(ejercicio2.distances_true[10], sys.maxsize)
        self.assertEqual(ejercicio2.distances_false[10], 0)

    def test_12(self):
        self.assertEqual(evaluate_condition(11, "In", 10, [1, 2, 3]), False)
        self.assertEqual(ejercicio2.distances_true[11], 7)
        self.assertEqual(ejercicio2.distances_false[11], 0)

    def test_13(self):
        self.assertEqual(evaluate_condition(12, "In", 10, [10]), True)
        self.assertEqual(ejercicio2.distances_true[12], 0)
        self.assertEqual(ejercicio2.distances_false[12], 1)

    def test_14(self):
        self.assertEqual(evaluate_condition(4, "Ge", 20, 10), True)
        self.assertEqual(ejercicio2.distances_true[4], 0)
        self.assertEqual(ejercicio2.distances_false[4], 11)

    def test_15(self):
        self.assertEqual(evaluate_condition(5, "Ge", 10, 20), False)
        self.assertEqual(ejercicio2.distances_true[5], 10)
        self.assertEqual(ejercicio2.distances_false[5], 0)

    def test_16(self):
        self.assertEqual(evaluate_condition(6, "Ge", 20, 20), True)
        self.assertEqual(ejercicio2.distances_true[6], 0)
        self.assertEqual(ejercicio2.distances_false[6], 1)

    def test_17(self):
        self.assertEqual(evaluate_condition(7, "Gt", 20, 10), True)
        self.assertEqual(ejercicio2.distances_true[7], 0)
        self.assertEqual(ejercicio2.distances_false[7], 10)

    def test_18(self):
        self.assertEqual(evaluate_condition(8, "Gt", 10, 20), False)
        self.assertEqual(ejercicio2.distances_true[8], 11)
        self.assertEqual(ejercicio2.distances_false[8], 0)

    def test_19(self):
        self.assertEqual(evaluate_condition(9, "Gt", 20, 20), False)
        self.assertEqual(ejercicio2.distances_true[9], 1)
        self.assertEqual(ejercicio2.distances_false[9], 0)
