from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.level = None
        self.ptr = None

    def add_edge(self, u, v, cap):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def bfs(self, source, sink):
        self.level = [-1] * self.n
        self.level[source] = 0
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        
        return self.level[sink] != -1

    def dfs(self, u, sink, flow):
        if u == sink or flow == 0:
            return flow
        
        while self.ptr[u] < len(self.adj[u]):
            v, cap, rev = self.adj[u][self.ptr[u]]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, sink, min(flow, cap))
                if pushed > 0:
                    self.adj[u][self.ptr[u]][1] -= pushed
                    self.adj[v][rev][1] += pushed
                    return pushed
            self.ptr[u] += 1
        
        return 0

    def max_flow(self, source, sink):
        flow = 0
        self.ptr = [0] * self.n
        while self.bfs(source, sink):
            print(self.level)
            pushed = self.dfs(source, sink, float('inf'))
            if pushed == 0 :
                self.ptr = [0] * self.n
            else:
                print("Pushed flow ", pushed)
            flow += pushed
        return flow

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

result = graph.max_flow(0,10)
print('Max flow: ', result)