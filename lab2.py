from itertools import combinations
class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.addVertex(vertex1)
        if vertex2 not in self.adj_list:
            self.addVertex(vertex2)
        
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def graphColoring(self):
        colors = {}
        for vertex in sorted(self.adj_list, key=lambda x: len(self.adj_list[x]), reverse=True):
            used_colors = {colors[neighbor] for neighbor in self.adj_list[vertex] if neighbor in colors}
            color = 1
            while color in used_colors:
                color += 1
            colors[vertex] = color
        return colors
    
    def isVertexCover(self, cover):
        edges = {(u, v) for u in self.adj_list for v in self.adj_list[u]}
        for u in cover:
            for v in self.adj_list[u]:
                edges -={(u,v)}
                edges -={(v,u)}
        return len(edges) == 0

    def minVertexCover(self):
        nodes = list(self.adj_list.keys())
        for r in range(1, len(nodes) + 1):
            for cover in combinations(nodes, r):
                if self.isVertexCover(set(cover)):
                    return set(cover)
        return set(nodes)

    def minEdgeCover(self):
        covered = set()
        edge_cover = []
        for u in self.adj_list:
            for v in self.adj_list[u]:
                if u not in covered and v not in covered:
                    edge_cover.append((u, v))
                    covered.add(u)
                    covered.add(v)
        for u in self.adj_list:
            if u not in covered and self.adj_list[u]:
                v = self.adj_list[u][0]
                edge_cover.append((u, v))
                covered.add(u)
                covered.add(v)
        return edge_cover    
    

g = Graph()
g.addEdge(2, 1)
g.addEdge(1, 4)
g.addEdge(4, 3)
g.addEdge(3, 11)
g.addEdge(2, 5)
g.addEdge(5, 4)
g.addEdge(2, 4)
g.addEdge(6, 5)
g.addEdge(6, 7)
g.addEdge(7, 10)
g.addEdge(10, 15)
g.addEdge(15, 7)
g.addEdge(14, 15)
g.addEdge(6, 14)
g.addEdge(5, 13)
g.addEdge(6, 9)
g.addEdge(9, 5)
g.addEdge(14, 9)
g.addEdge(9, 13)
g.addEdge(14, 13)
g.addEdge(17, 13)
g.addEdge(17, 16)
g.addEdge(16, 12)
g.addEdge(17, 12)
g.addEdge(13, 12)
g.addEdge(12, 8)
g.addEdge(4, 8)
g.addEdge(12, 11)
g.addEdge(11, 8)
g.addEdge(5, 8)
g.addEdge(13, 8)

vc = g.minVertexCover()
ec = g.minEdgeCover()
colors = g.graphColoring()

print('Vertex cover ', vc)
print('Edge cover ', ec)
print('Vertex colors ', colors)