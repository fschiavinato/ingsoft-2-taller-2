import random
from typing import Tuple

def crossover(parent1: str, parent2: str, p_crossover=0.5) -> Tuple[str, str]:
    if not (p_crossover > random.random()):
        return parent1, parent2
    l = min(len(parent1), len(parent2))
    i = random.randint(0, l)
    offspring1 = parent1[:i] + parent2[i:]
    offspring2 = parent2[:i] + parent1[i:]
    return offspring1, offspring2
