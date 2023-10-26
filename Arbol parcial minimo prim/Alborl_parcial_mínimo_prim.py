import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Árbol Parcial Mínimo (Prim):")
        mst = nx.Graph()
        for i in range(1, self.V):
            print(f"Arista: ({parent[i]}, {i}) Peso: {self.graph[i][parent[i]]}")
            mst.add_edge(parent[i], i, weight=self.graph[i][parent[i]])

        pos = nx.spring_layout(mst)
        labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw(mst, pos, with_labels=True, node_color='lightblue')
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
        plt.show()

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

            self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    g.prim_mst()
