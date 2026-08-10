import random

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(path):
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]
    total += graph[path[-1]][path[0]] 
    return total

def neighbour(path):
    new_path = path[:]
    i, j = random.sample(range(1, len(path)), 2)  
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def hill_climbing(max_iterations=1000, neighbors_per_step=100):
    current = [0, 1, 2, 3]
    current_cost = cost(current)

    for _ in range(max_iterations):
        neighbors = [neighbour(current) for _ in range(neighbors_per_step)]
        best_neighbor = min(neighbors, key=cost)
        best_cost = cost(best_neighbor)

        if best_cost < current_cost:
            current, current_cost = best_neighbor, best_cost
        else:
            break

    return current, current_cost

path, minimum_cost = hill_climbing()

print("Best Path:", path + [path[0]])
print("Minimum Cost:", minimum_cost)
