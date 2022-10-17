import random
from ejercicio5 import chars


def mutate(individual: str) -> str:
    l = len(individual)
    i = random.randint(0, l)
    if random.random() < 0.5:
        # Agregamos
        if l < 10:
            return individual[:i] + random.choice(chars) + individual[i:]  
    else:
        # Removemos
        if l > 1:
            return individual[:i] + individual[i + 1 :]

    return individual

