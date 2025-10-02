import itertools
import math

def bt_knapsack(items, capacity):
    n = len(items)
    max_value = 0
    best_subset = []
    for r in range(n + 1):
        for subset in itertools.combinations(range(n), r):
            total_value = sum(items[i][0] for i in subset)
            total_weight = sum(items[i][1] for i in subset)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_subset = [items[i][2] for i in subset]
    return best_subset, max_value

def bt_tsp(cities):
    n = len(cities)
    if n == 0:
        return []
    min_dist = float('inf')
    best_tour = None
    for perm in itertools.permutations(range(1, n)):
        tour = [0] + list(perm)
        dist = sum(math.dist(cities[tour[i]], cities[tour[i+1]]) for i in range(n-1)) + math.dist(cities[tour[-1]], cities[tour[0]])
        if dist < min_dist:
            min_dist = dist
            best_tour = tour
    return best_tour, min_dist
