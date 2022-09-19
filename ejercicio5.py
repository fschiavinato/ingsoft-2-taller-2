import random
import string

chars = (
    string.ascii_uppercase + string.ascii_lowercase + string.digits + "+" + "%" + " "
)


def create_population(population_size: int):
    string_random = lambda: "".join(random.choice(chars) for _ in range(10))
    return [string_random() for _ in range(population_size)]
