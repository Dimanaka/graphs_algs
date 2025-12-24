import math
import random

# Функція для обчислення вартості маршруту
def route_cost(route, dist_matrix):
    cost = 0
    n = len(route)
    for i in range(n):
        a = route[i]
        b = route[(i + 1) % n]  # Використовується модуль для циклічності маршруту
        d = dist_matrix[a][b]
        if d == float('inf'):
            return float('inf')  # Якщо маршрут недопустимий, повертаємо нескінченність
        cost += d
    return cost

# Алгоритм імітації відпалу для знаходження оптимального маршруту
def simulated_annealing(dist_matrix, initial_temp=20, cooling_rate=0.99, stop_temp=1, max_iter=100000):
    n = len(dist_matrix)
    current_route = list(range(n))  
    random.shuffle(current_route)  # Ініціалізація маршруту
    
    # Генеруємо допустимий початковий маршрут
    while route_cost(current_route, dist_matrix) == float('inf'):
        random.shuffle(current_route)

    best_route = list(current_route)  # Початковий маршрут
    best_cost = route_cost(best_route, dist_matrix)  # Його вартість
    current_cost = best_cost
    temp = initial_temp  # Початкова температура
    iteration = 0

    print(f'Initial route {best_route} cost, {best_cost}')
    
    # Головний цикл алгоритму імітації відпалу
    while temp > stop_temp and iteration < max_iter:
        i, j = random.sample(range(n), 2)  # Випадково вибираємо дві точки для обміну
        new_route = list(current_route)
        new_route[i], new_route[j] = new_route[j], new_route[i]  # Обмін точками
        new_cost = route_cost(new_route, dist_matrix)

        if new_cost == float('inf'):
            iteration += 1
            continue  # Якщо маршрут недопустимий, пропускаємо ітерацію
        
        #print(f'New route: {new_route} cost {new_cost}')
        #print(f"Temperature {temp}")
        
        # Розрахунок зміни вартості та прийняття рішення про оновлення маршруту
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            print(f'New approved route: {new_route} cost {new_cost}')
            print(f"Temperature {temp}")
            current_route = new_route
            current_cost = new_cost
            if current_cost < best_cost:
                print('This is current minimal route')
                best_route = list(current_route)
                best_cost = current_cost

        temp *= cooling_rate  # Охолодження системи
        iteration += 1

    return best_route, best_cost  # Повертаємо найкращий знайдений маршрут і його вартість

# Матриця суміжності
dist_matrix = [
    [0, 76, 97, 30, float('inf'), float('inf'), float('inf'), float('inf')],
    [76, 0, 16, float('inf'), 9, float('inf'), float('inf'), float('inf')],
    [97, 16, 0, 59, 60, 51, 11, float('inf')],
    [30, float('inf'), 59, 0, float('inf'), float('inf'), 6, float('inf')],
    [float('inf'), 9, 60, float('inf'), 0, 42, float('inf'), 12],
    [float('inf'), float('inf'), 51, float('inf'), 42, 0, 56, 96],
    [float('inf'), float('inf'), 11, 6, float('inf'), 56, 0, 36],
    [float('inf'), float('inf'), float('inf'), float('inf'), 12, 96, 36, 0]
]

# Виконання алгоритму імітації відпалу
best_route, best_distance = simulated_annealing(dist_matrix)

# Вивід результату
if best_distance == float('inf'):
    print("There are no route")  # Якщо немає можливих маршрутів
else:
    print("Best route: ", best_route)
    print("Route cost: ", best_distance)