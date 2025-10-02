import math

def dc_knapsack(items, capacity):
    def knapsack_recursive(index, cap):
        if index == len(items) or cap == 0:
            return [], 0
        value, weight, name = items[index]
        excl, excl_val = knapsack_recursive(index + 1, cap)
        if weight <= cap:
            incl, incl_val = knapsack_recursive(index + 1, cap - weight)
            incl_val += value
            incl = [name] + incl
            if incl_val > excl_val:
                return incl, incl_val
        return excl, excl_val

    selected, total_value = knapsack_recursive(0, capacity)
    return selected, total_value

def dc_tsp(cities):
    n = len(cities)
    if n <= 1:
        return list(range(n)), 0.0
    # Simple insertion heuristic: start with 0-1, insert others at best position
    tour = [0, 1]
    remaining = list(range(2, n))
    for city in remaining:
        min_increase = float('inf')
        best_pos = -1
        for pos in range(1, len(tour) + 1):
            new_tour = tour[:pos] + [city] + tour[pos:]
            increase = math.dist(cities[new_tour[pos-1]], cities[city]) + math.dist(cities[city], cities[new_tour[pos]]) - math.dist(cities[new_tour[pos-1]], cities[new_tour[pos]])
            if increase < min_increase:
                min_increase = increase
                best_pos = pos
        tour.insert(best_pos, city)
    total_dist = sum(math.dist(cities[tour[i]], cities[tour[(i+1) % n]]) for i in range(n))
    return tour, total_dist
