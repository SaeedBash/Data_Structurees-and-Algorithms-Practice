from collections import defaultdict
import os

def clear_screen():
    # 'nt' refers to Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' refers to Linux, macOS, Unix, etc.
    else:
        _ = os.system('clear')

class GNode: #Graph nodes
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self, directed = False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph.keys():
            self.graph[v] = []
        if not self.directed:
            self.graph[v].append(u)
        
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    def __str__(self):
        return str(dict(self.graph))
    
    def print_adj_matrix(self):
        print("Keys", end='\t')
        for key in self.graph.keys():
            print(f"[{key}]", end='\t')
        print()
        for key in self.graph.keys():
            print(f"[{key}]", end='\t')
            for neighbor in self.graph.keys():
                if neighbor in g.get_neighbors(key):
                    print(" 1", end='\t')
                else:
                    print(" 0", end='\t')
            print()

clear_screen()

#Tests

g = Graph()                 # Not Directional
# g = Graph (directed=True)   # Directional
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print(f"Neighbors of 1: {g.get_neighbors(1)}")
print(f"Full Graph Structure: {g}")

g.print_adj_matrix()
