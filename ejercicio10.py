from ejercicio5 import create_population
from ejercicio6 import evaluate_population
from ejercicio7 import selection
from ejercicio8 import crossover
from ejercicio9 import mutate


def genetic_algorithm():
    eps = 1e-5
    generation = 0
    population = create_population(10)
    evaluated_population = evaluate_population(population)
    best_individual, fitness_best_individual = min(
        evaluated_population.items(), key=lambda t: t[1]
    )
    print(f'best_individual "{best_individual}" with score:  {fitness_best_individual}')

    # Continuar mientras la cantidad de generaciones es menor que 1000
    # o no se haya encontrado un m\’inimo global
    while fitness_best_individual > eps and generation < 1000:
        # Producir una nueva poblaci’on con el mismo tama˜no que
        # la generaci’on anterior,usar selection,crossover y mutation
        new_population = []
        for _ in range(len(population) // 2):

            p, m = (selection(evaluated_population, 10) for _ in range(2))
            h1, h2 = crossover(p, m)
            h1 = mutate(h1)
            h2 = mutate(h2)
            new_population.append(h1),
            new_population.append(h2)

        # Una vez creada,reemplazar la poblaci’on anterior con la nueva
        # poblacion
        generation += 1
        population = new_population

        # Evaluar la nueva poblaci’one imprimir el mejor valor de fitness
        evaluated_population = evaluate_population(population)
        best_individual, fitness_best_individual = min(
            evaluated_population.items(), key=lambda t: t[1]
        )
        print(
            f'best_individual "{best_individual}" with score:  {fitness_best_individual}'
        )


if __name__ == "__main__":
    genetic_algorithm()
