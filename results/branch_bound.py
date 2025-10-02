
import math

def bb_knapsack(items, capacity):
    n = len(items)
    if n == 0:
        return [], 0
    sorted_items = sorted(enumerate(items), key=lambda x: x[1][0] / x[1][1], reverse=True)
    max_value = [0]
    best_subset = [[]]

    def bound(i, current_weight, current_value):
        if current_weight >= capacity:
            return current_value
        bound_val = current_value
        j = i
        w = current_weight
        while j < n and w + sorted_items[j][1][1] <= capacity:
            bound_val += sorted_items[j][1][0]
            w += sorted_items[j][1][1]
            j += 1
        if j < n:
            bound_val += (capacity - w) * (sorted_items[j][1][0] / sorted_items[j][1][1])
        return bound_val

    def search(i, current_weight, current_value, taken):
        if i == n:
            if current_value > max_value[0]:
                max_value[0] = current_value
                best_subset[0] = taken[:]
            return
        if bound(i, current_weight, current_value) <= max_value[0]:
            return
        search(i + 1, current_weight, current_value, taken)
        if current_weight + sorted_items[i][1][1] <= capacity:
            taken.append(sorted_items[i][1][2])
            search(i + 1, current_weight + sorted_items[i][1][1], current_value + sorted_items[i][1][0], taken)
            taken.pop()

    search(0, 0, 0, [])
    return best_subset[0], max_value[0]

def bb_tsp(cities):
    n = len(cities)
    if n <= 1:
        return list(range(n)), 0.0
    dist = [[math.dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    min_cost = [float('inf')]
    best_tour = [None]

    def bound(state, last, cost):
        # Lower bound: cost + min edges from last to unvisited + min edges between unvisited
        unvisited = [j for j in range(1, n) if not (state & (1 << j))]
        if not unvisited:
            return cost + dist[last][0]
        min_to_unvisited = min(dist[last][j] for j in unvisited) if unvisited else 0
        # Simplified: just add min to unvisited; full MST bound is complex
        return cost + min_to_unvisited

    def search(state, last, cost, path):
        if state == (1 << n) - 1:
            total_cost = cost + dist[last][0]
            if total_cost < min_cost[0]:
                min_cost[0] = total_cost
                best_tour[0] = path + [0]
            return
        if bound(state, last, cost) >= min_cost[0]:
            return
        for next_city in range(1, n):
            if not (state & (1 << next_city)):
                new_state = state | (1 << next_city)
                search(new_state, next_city, cost + dist[last][next_city], path + [next_city])

    search(1, 0, 0, [0])
    return best_tour[0], min_cost[0]
