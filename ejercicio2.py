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

