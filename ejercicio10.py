import random, datetime
import ejercicio2
from ejercicio3 import cgi_decoded_instrumented
from ejercicio5 import create_population
from ejercicio6 import evaluate_population
from ejercicio7 import selection
from ejercicio8 import crossover
from ejercicio9 import mutate 

seed = int(datetime.datetime.now().timestamp())

def genetic_algorithm():
    population_size = 100
    tournament_size = 5
    p_crossover = 0.70
    p_mutation = 0.20

    eps = 1e-5
    generation = 0
    population = create_population(population_size)
    evaluated_population = evaluate_population(population)
    best_individual, fitness_best_individual = min(
        evaluated_population.items(), key=lambda t: t[1]
    )
    printGenerationInfo(generation, best_individual, fitness_best_individual)

    # Continuar mientras la cantidad de generaciones es menor que 1000
    # o no se haya encontrado un minimo global
    while fitness_best_individual > eps and generation < 1000:
        # Producir una nueva poblacion con el mismo tamanio que
        # la generacion anterior, usar selection, crossover y mutation
        new_population = []
        for _ in range(len(population) // 2):

            p, m = (selection(evaluated_population, tournament_size) for _ in range(2))
            h1, h2 = crossover(p, m) if random.random() < p_crossover  else (p, m)
            h1 = mutate(h1) if random.random() < p_mutation else h1
            h2 = mutate(h2) if random.random() < p_mutation else h2
            new_population.append(h1)
            new_population.append(h2)

        # Una vez creada, reemplazar la poblacion anterior con la nueva poblacion
        generation += 1
        population = new_population

        # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
        evaluated_population = evaluate_population(population)
        best_individual, fitness_best_individual = min(
            evaluated_population.items(), key=lambda t: t[1]
        )
        printGenerationInfo(generation, best_individual, fitness_best_individual)
    return best_individual

def printGenerationInfo(generation, best_individual, fitness_best_individual):
    print(f'> Generation {generation}: best_individual "{best_individual}" with score: {fitness_best_individual}')

def getBranchCoverage(individual):
    ejercicio2.distances_true = {}
    ejercicio2.distances_false = {}
    try: 
        cgi_decoded_instrumented(individual)
    except:
        pass

    # Mediante las distances podemos saber si pasaron por la branch
    sumBranchesPassed = 0
    for i in range(1, 4):
        if ejercicio2.distances_true.get(i) == 0:
            sumBranchesPassed += 1 
        if ejercicio2.distances_false.get(i) == 0:
            sumBranchesPassed += 1

    # Las ultimas dos condiciones como estan juntas por un AND 
    # las tomamos como la misma branch
    if ejercicio2.distances_true.get(4) == 0 and ejercicio2.distances_true.get(5) == 0:
        sumBranchesPassed += 1

    if ejercicio2.distances_false.get(4) == 0 and ejercicio2.distances_false.get(5) == 0:
            sumBranchesPassed += 1

    return sumBranchesPassed/8
    


if __name__ == "__main__":
    random.seed(seed)
    print(f'Seed: {seed}')
    best_individual = genetic_algorithm()
    print(f'Best individual coverage: {getBranchCoverage(best_individual)*100}%')
