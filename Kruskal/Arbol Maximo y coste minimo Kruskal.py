import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda x: x[2])
        minimum_tree = []
        maximum_tree = []

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for i, edge in enumerate(self.edges):
            u, v, w = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                minimum_tree.append(edge)
                maximum_tree.append(edge)
                self.union(parent, rank, root_u, root_v)

                # Dibuja el grafo actual en cada paso
                plt.figure(figsize=(10, 5))
                plt.subplot(121)
                plt.title("Árbol de Mínimo Costo (Kruskal)")
                for u, v, w in minimum_tree:
                    plt.plot([u, v], [v, u], 'bo-')
                plt.subplot(122)
                plt.title("Árbol de Máximo Costo (Kruskal)")
                for u, v, w in maximum_tree[::-1]:
                    plt.plot([u, v], [v, u], 'ro-')
                plt.show()

                # Imprime el progreso en la consola
                print(f'Paso {i + 1}: Agregada arista ({u}, {v}) con peso {w}')

        # Imprime los árboles de máximo y mínimo costo
        print("\nÁrbol de Mínimo Costo (Kruskal):")
        for u, v, w in minimum_tree:
            print(f'({u} - {v}): {w}')

        print("\nÁrbol de Máximo Costo (Kruskal):")
        for u, v, w in maximum_tree[::-1]:
            print(f'({u} - {v}): {w}')

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal()
