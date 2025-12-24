from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Кількість вершин
        self.graph = defaultdict(dict)  # Представлення графа через словник

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity  # Пропускна здатність ребра
        self.graph[v][u] = 0  # Зворотне ребро з нульовою початковою пропускною здатністю

    def dfs(self, source, sink, flow, visited, scale):
        if source == sink:
            return flow
        
        visited.add(source)
        for neighbor, capacity in self.graph[source].items():
            if neighbor not in visited and capacity >= scale:  # Враховуємо масштабування
                min_flow = min(flow, capacity)
                pushed_flow = self.dfs(neighbor, sink, min_flow, visited, scale)
                
                if pushed_flow > 0:
                    self.graph[source][neighbor] -= pushed_flow
                    self.graph[neighbor][source] += pushed_flow
                    return pushed_flow
        return 0
    
    def max_flow(self, source, sink):
        max_capacity = max(n for n in self.graph[0].values())
        scale = 1
        while scale * 2 <= max_capacity:
            scale *= 2
        
        max_flow = 0
        while scale > 0:
            
            while True:
                visited = set()
                flow = self.dfs(source, sink, float('inf'), visited, scale)
                if flow == 0:
                    break
                print("pushed flow: ", flow)
                max_flow += flow
            scale //= 2
            print('change scale')
        return max_flow

# Задаємо граф
graph = Graph(11)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 10)
graph.add_edge(1, 4, 15)
graph.add_edge(2, 1, 14)
graph.add_edge(2, 5, 20)
graph.add_edge(3, 6, 12)
graph.add_edge(4, 5, 6)
graph.add_edge(4, 7, 10)
graph.add_edge(5, 3, 5)
graph.add_edge(6, 8, 7)
graph.add_edge(6, 9, 10)
graph.add_edge(7, 10, 5)
graph.add_edge(8, 4, 15)
graph.add_edge(8, 7, 4)
graph.add_edge(8, 10, 15)
graph.add_edge(9, 10, 10)

source, sink = 0, 10
print("Max flow with scaling:", graph.max_flow(source, sink))
