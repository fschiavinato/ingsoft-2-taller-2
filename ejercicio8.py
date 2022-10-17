import random
from typing import Tuple

def crossover(parent1: str, parent2: str) -> Tuple[str, str]:
    i = random.randint(0, len(parent1))
    j = random.randint(0, len(parent2))
    offspring1 = parent1[:i] + parent2[j:]
    offspring2 = parent2[:j] + parent1[i:]
    return offspring1[:10], offspring2[:10]
