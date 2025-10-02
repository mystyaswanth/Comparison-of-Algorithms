import math

def greedy_knapsack(items, capacity):
    sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    selected = []
    total_value = 0
    current_weight = 0
    for value, weight, name in sorted_items:
        if current_weight + weight <= capacity:
            selected.append(name)
            total_value += value
            current_weight += weight
    return selected, total_value

def greedy_tsp(cities):
    n = len(cities)
    if n == 0:
        return []
    visited = [False] * n
    tour = [0]  # Start from city 0
    visited[0] = True
    for _ in range(n - 1):
        last = tour[-1]
        min_dist = float('inf')
        next_city = -1
        for i in range(n):
            if not visited[i]:
                dist = math.dist(cities[last], cities[i])
                if dist < min_dist:
                    min_dist = dist
                    next_city = i
        tour.append(next_city)
        visited[next_city] = True
    total_dist = sum(math.dist(cities[tour[i]], cities[tour[i+1]]) for i in range(n-1)) + math.dist(cities[tour[-1]], cities[tour[0]])
    return tour, total_dist
