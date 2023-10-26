
import sys
import matplotlib.pyplot as plt

# Función para encontrar el vértice no visitado con la distancia mínima
def min_distance(distances, visited):
    min_dist = sys.maxsize
    min_index = -1

    for v in range(len(distances)):
        if distances[v] < min_dist and not visited[v]:
            min_dist = distances[v]
            min_index = v

    return min_index

# Función para imprimir la solución
def print_solution(distances):
    print("Vértice \t Distancia desde el origen")
    for node in range(len(distances)):
        print(f"{node} \t\t {distances[node]}")

# Implementación del algoritmo de Dijkstra con representación gráfica
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[source] = 0
    visited = [False] * num_vertices

    plt.ion()  # Habilita la interactividad en Matplotlib

    for _ in range(num_vertices):
        u = min_distance(distances, visited)
        visited[u] = True

        for v in range(num_vertices):
            if not visited[v] and graph[u][v] and distances[u] != sys.maxsize and (distances[u] + graph[u][v]) < distances[v]:
                distances[v] = distances[u] + graph[u][v]
                print_solution(distances)

                # Agrega un gráfico de barras para visualizar las distancias actualizadas
                plt.bar(range(num_vertices), distances)
                plt.title(f"Paso {_ + 1}")
                plt.pause(1)
                plt.clf()  # Limpia el gráfico para el próximo paso

    plt.ioff()  # Desactiva la interactividad al final

# Ejemplo de un grafo representado como matriz de adyacencia
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 2],
    [0, 0, 1, 2, 0]
]

source_vertex = 0  # Vértice de inicio

print("Simulación del Algoritmo de Dijkstra:")
dijkstra(graph, source_vertex)

plt.show()  # Muestra el gráfico final