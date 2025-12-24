import numpy as np

def tsp_branch_and_bound(graph):
    n = len(graph)
    best_cost = float('inf')
    best_path = []

    def branch_and_bound(path, cost):
        nonlocal best_cost, best_path
        if len(path) == n:
            cost += graph[path[-1]][path[0]] 
            if cost < best_cost:
                best_cost = cost
                best_path = path[:]
            return

        for i in range(n):
            if i not in path:
                new_cost = cost + graph[path[-1]][i]
                if new_cost < best_cost:  
                    path.append(i)
                    branch_and_bound(path, new_cost)
                    path.pop()

    
    branch_and_bound([0], 0)

    return best_cost, best_path

# Приклад графа (матриця вартостей)
graph = np.array([
    [float('inf'), 29, 29, 33, 40],
    [32, float('inf'), 30, 40, 37],
    [44, 28, float('inf'), 32, 26],
    [47, 38, 44, float('inf'), 47],
    [44, 37, 33, 32, float('inf')]
])

best_cost, best_path = tsp_branch_and_bound(graph)
print(f"Best path: {best_path}")
print(f"Best cost: {best_cost}")