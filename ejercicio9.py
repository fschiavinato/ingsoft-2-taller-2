import random
from ejercicio5 import chars


def mutate(individual: str) -> str:
    p = 0.5
    l = len(individual)
    i = random.randint(0, l)
    if p > random.random() and l < 10:
        return individual[:i] + random.choice(chars) + individual[i:]
    elif l > 1:
        return individual[:i] + individual[i + 1 :]

