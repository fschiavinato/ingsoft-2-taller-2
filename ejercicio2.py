from typing import Dict
import sys

# Inicializar mappings globales

distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num, d_true, d_false):
    global distances_true, distances_false
    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def evaluate_condition(condition_num: int, op: str, lhs: int, rhs: int) -> bool:
    if op == "Eq":
        if lhs == rhs:
            update_maps(condition_num, abs(lhs - rhs), 1)
        else:
            update_maps(condition_num, abs(lhs - rhs), 0)
        return lhs == rhs

    if op == "Ne":
        if lhs == rhs:
            update_maps(condition_num, 1, abs(lhs - rhs))
        else:
            update_maps(condition_num, 0, abs(lhs - rhs))
        return lhs != rhs

    if op == "Lt":
        if lhs < rhs:
            update_maps(condition_num, 0, rhs - lhs)
        else:
            update_maps(condition_num, lhs - rhs + 1, 0)
        return lhs < rhs

    if op == "Gt":
        if lhs > rhs:
            update_maps(condition_num, 0, lhs - rhs)
        else:
            update_maps(condition_num, rhs - lhs + 1, 0)
        return lhs > rhs

    if op == "Le":
        if lhs <= rhs:
            update_maps(condition_num, 0, rhs - lhs + 1)
        else:
            update_maps(condition_num, lhs - rhs, 0)
        return lhs <= rhs

    if op == "Ge":
        if lhs >= rhs:
            update_maps(condition_num, 0, lhs - rhs + 1)
        else:
            update_maps(condition_num, rhs - lhs, 0)
        return lhs >= rhs

    if op == "In":
        d = min([abs(x - lhs) for x in rhs] + [sys.maxsize])
        if lhs in rhs:
            update_maps(condition_num, d, 1)
        else:
            update_maps(condition_num, d, 0)
        return lhs in rhs


import unittest


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(evaluate_condition(0, "Eq", 20, 10), False)
        self.assertEqual(distances_true[0], 10)
        self.assertEqual(distances_false[0], 0)

    def test_2(self):
        self.assertEqual(evaluate_condition(1, "Eq", 20, 20), True)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def test_3(self):
        self.assertEqual(evaluate_condition(2, "Ne", 20, 10), True)
        self.assertEqual(distances_true[2], 0)
        self.assertEqual(distances_false[2], 10)

    def test_4(self):
        self.assertEqual(evaluate_condition(3, "Ne", 20, 20), False)
        self.assertEqual(distances_true[3], 1)
        self.assertEqual(distances_false[3], 0)

    def test_5(self):
        self.assertEqual(evaluate_condition(4, "Le", 10, 20), True)
        self.assertEqual(distances_true[4], 0)
        self.assertEqual(distances_false[4], 11)

    def test_6(self):
        self.assertEqual(evaluate_condition(5, "Le", 20, 10), False)
        self.assertEqual(distances_true[5], 10)
        self.assertEqual(distances_false[5], 0)

    def test_7(self):
        self.assertEqual(evaluate_condition(6, "Le", 20, 20), True)
        self.assertEqual(distances_true[6], 0)
        self.assertEqual(distances_false[6], 1)

    def test_8(self):
        self.assertEqual(evaluate_condition(7, "Lt", 10, 20), True)
        self.assertEqual(distances_true[7], 0)
        self.assertEqual(distances_false[7], 10)

    def test_9(self):
        self.assertEqual(evaluate_condition(8, "Lt", 20, 10), False)
        self.assertEqual(distances_true[8], 11)
        self.assertEqual(distances_false[8], 0)

    def test_10(self):
        self.assertEqual(evaluate_condition(9, "Lt", 20, 20), False)
        self.assertEqual(distances_true[9], 1)
        self.assertEqual(distances_false[9], 0)

    def test_11(self):
        self.assertEqual(evaluate_condition(10, "In", 10, []), False)
        self.assertEqual(distances_true[10], sys.maxsize)
        self.assertEqual(distances_false[10], 0)

    def test_12(self):
        self.assertEqual(evaluate_condition(11, "In", 10, [1, 2, 3]), False)
        self.assertEqual(distances_true[11], 7)
        self.assertEqual(distances_false[11], 0)

    def test_13(self):
        self.assertEqual(evaluate_condition(12, "In", 10, [10]), True)
        self.assertEqual(distances_true[12], 0)
        self.assertEqual(distances_false[12], 1)

    def test_14(self):
        self.assertEqual(evaluate_condition(4, "Ge", 20, 10), True)
        self.assertEqual(distances_true[4], 0)
        self.assertEqual(distances_false[4], 11)

    def test_15(self):
        self.assertEqual(evaluate_condition(5, "Ge", 10, 20), False)
        self.assertEqual(distances_true[5], 10)
        self.assertEqual(distances_false[5], 0)

    def test_16(self):
        self.assertEqual(evaluate_condition(6, "Ge", 20, 20), True)
        self.assertEqual(distances_true[6], 0)
        self.assertEqual(distances_false[6], 1)

    def test_17(self):
        self.assertEqual(evaluate_condition(7, "Gt", 20, 10), True)
        self.assertEqual(distances_true[7], 0)
        self.assertEqual(distances_false[7], 10)

    def test_18(self):
        self.assertEqual(evaluate_condition(8, "Gt", 10, 20), False)
        self.assertEqual(distances_true[8], 11)
        self.assertEqual(distances_false[8], 0)

    def test_19(self):
        self.assertEqual(evaluate_condition(9, "Gt", 20, 20), False)
        self.assertEqual(distances_true[9], 1)
        self.assertEqual(distances_false[9], 0)
