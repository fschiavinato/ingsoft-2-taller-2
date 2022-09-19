import random
from typing import Dict


def selection(evaluated_population: Dict[str, float], tournament_size):
    tournament = random.choices(list(evaluated_population.keys()), k=tournament_size)
    max_fitness = min(evaluated_population[player] for player in tournament)
    return next(
        player for player in tournament if evaluated_population[player] == max_fitness
    )


