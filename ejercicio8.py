import random
from typing import Tuple

def crossover(parent1: str, parent2: str) -> Tuple[str, str]:
    l = min(len(parent1), len(parent2))
    children1 = list(parent1)
    children2 = list(parent2)
    for i in range(l):
        if random.randint(0, 1) == 0:
            children1[i] = parent2[i]
            children2[i] = parent1[i]

    return "".join(children1), "".join(children2)
