import random
from ejercicio5 import chars


def mutate(individual: str, probability = 0.5) -> str:
    l = len(individual)
    i = random.randint(0, l)
    if probability > random.random() and l < 10:
        return individual[:i] + random.choice(chars) + individual[i:]
    elif l > 1:
        return individual[:i] + individual[i + 1 :]

