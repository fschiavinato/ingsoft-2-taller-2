from ejercicio3 import cgi_decoded_instrumented
import ejercicio2


def get_fitness_cgi_decode(s: str) -> float:
    try:
        cgi_decoded_instrumented(s)
    except:
        pass
    max_branch = max(ejercicio2.distances_true.keys())
    approach_level = 5 - max_branch
    if max_branch == 2:
        branch_distance = ejercicio2.distances_false[max_branch]
    else:
        branch_distance = ejercicio2.distances_true[max_branch]

    normalized_branch_distance = branch_distance / (branch_distance + 1)

    return approach_level + normalized_branch_distance


