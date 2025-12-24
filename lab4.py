
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        transposed = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed.add_edge(neighbor, node)
        return transposed

    def fill_order(self, visited, stack):
        for i in range(1, self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

    def dfs_scc(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_scc(neighbor, visited, component)

    def find_sccs(self):
        stack = []
        visited = [False] * (self.V + 1)

        # 1. Виконуємо DFS і запам’ятовуємо порядок завершення
        self.fill_order(visited, stack)
        print(stack)
        # 2. Транспонуємо граф
        transposed = self.transpose()

        # 3. Виконуємо DFS на транспонованому графі
        visited = [False] * (self.V + 1)
        sccs = []
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed.dfs_scc(node, visited, component)
                sccs.append(component)
        
        return sccs


# Приклад використання
g = Graph(18)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(4, 3)
g.add_edge(3, 11)
g.add_edge(2, 5)
g.add_edge(5, 4)
g.add_edge(2, 4)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(7, 10)
g.add_edge(10, 15)
g.add_edge(15, 7)
g.add_edge(14, 15)
g.add_edge(6, 14)
g.add_edge(5, 13)
g.add_edge(6, 9)
g.add_edge(9, 5)
g.add_edge(14, 9)
g.add_edge(9, 13)
g.add_edge(14, 13)
g.add_edge(17, 13)
g.add_edge(17, 16)
g.add_edge(16, 12)
g.add_edge(17, 12)
g.add_edge(13, 12)
g.add_edge(12, 8)
g.add_edge(4, 8)
g.add_edge(12, 11)
g.add_edge(11, 8)
g.add_edge(5, 8)
g.add_edge(13, 8)

sccs = g.find_sccs()
print("Strongly conected components", sccs)
