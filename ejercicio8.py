import random
from typing import Tuple


def crossover(parent1: str, parent2: str) -> Tuple[str, str]:
    l = min(len(parent1), len(parent2))
    i = random.randint(0, l)
    offspring1 = parent1[:i] + parent2[i:]
    offspring2 = parent2[:i] + parent1[i:]
    return offspring1, offspring2


