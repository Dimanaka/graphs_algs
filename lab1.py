from collections import deque

import sys
sys.stdout.reconfigure(encoding='utf-8')

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.addVertex(vertex1)
        if vertex2 not in self.adj_list:
            self.addVertex(vertex2)
        
        self.adj_list[vertex1].add(vertex2)
        self.adj_list[vertex2].add(vertex1)
    
    def BFS(self, start, target):
        queue = deque([[start]])  # Черга з шляхами
        visited = [start]    # Відвідані вершини

        while queue:
            path = queue.popleft()     
            node = path[-1]

            if node == target:
                return path

            for neighbor in self.adj_list.get(node, []):  # Отримуємо сусідів
                if neighbor not in visited:
                    visited.append(neighbor) 
                    queue.append(path + [neighbor])  # Додаємо новий шлях

        return None  # Якщо шляху немає
    
    def buildPathLenMatrix(self):
        n = len(self.adj_list)
        pathLenMatrix = [[0] * n for _ in range(n)]

        for i  in range(n):
            for j  in range(n):
                result = self.BFS(i + 1, j + 1)
                if result is not None:
                    pathLenMatrix[i][j] = len(result) - 1
        return pathLenMatrix

    def calculteSpecs(self, matrix):
        lenMaxes = []
        centralV = []
        peripheralV = []

        for row in matrix:
            lenMaxes.append(max(row))
        R = min(lenMaxes)
        D = max(lenMaxes)
        for i, row in enumerate(matrix):
            if max(row) == D:
                centralV.append(i + 1)
            elif max(row) == R:
                peripheralV.append(i + 1)
        return (R, D, centralV, peripheralV)


g = Graph()

# Задаємо граф за допомогою ребер
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(5,1)
g.addEdge(5,6)
g.addEdge(5,8)
g.addEdge(6,7)
g.addEdge(7,8)
g.addEdge(8,1)

matrix = g.buildPathLenMatrix()

print("Матриця відстаней")
for row in matrix:
    print(row)

(R, D, centralV, peripheralV) = g.calculteSpecs(matrix)

print("Діаметр: ", D)
print("Радіус: " , R)

print("Центаральні вершини: ", centralV)
print("Периферійні вершини: ", peripheralV)