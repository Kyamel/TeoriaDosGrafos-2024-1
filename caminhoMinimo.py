import time
from typing import List, Tuple
from listaAdjacencias import ListaAdjacencias


def caminhoMinDijkstra(grafo: ListaAdjacencias, origem: int, destino: int) -> Tuple[List[int], int, float]:
    """
    Calcula o caminho mínimo do vértice de origem até o vértice de destino usando o algoritmo de Dijkstra.

    Returns
        - caminho (List[int]): O caminho da origem até o destino no formato de uma lista de inteiros representando cada vértice.
        - custo (int): O custo total do caminho mínimo.
        - tempo (float): O tempo de execução do algoritmo em segundos.
    """

    start = time.time()

    dist = [float('inf')] * grafo.numVertices # float('inf') é uma forma de representar infinito em Python
    prev = [None] * grafo.numVertices

    dist[origem] = 0
    prev[origem] = origem

    O = set(range(grafo.numVertices)) # set é uma forma de representar conjuntos em Python
    C = set()

    while C != set(range(grafo.numVertices)):

        menor = float('inf')
        u = None
        for v in O:
            if dist[v] < menor:
                menor = dist[v]
                u = v
        if u is None:
            break
        
        C.add(u)
        O.remove(u)
        if u == destino:
            break

        for v, peso in grafo.vizinhos(u):
            if v not in C:
                if dist[v] > dist[u] + peso:
                    dist[v] = dist[u] + peso
                    prev[v] = u

    end = time.time()

    # Construindo o caminho do destino até a origem
    caminho = []
    atual = destino
    while atual != origem:
        caminho.append(atual)
        atual = prev[atual]
        if atual is None:
            return None, float('inf'), end - start
        
    caminho.append(origem)
    caminho.reverse()
    
    return caminho, dist[destino], end - start

def caminhoMinBellmanFord(grafo: ListaAdjacencias, origem: int, destino: int) -> Tuple[List[int], int, float]:
    """
    Calcula o caminho mínimo do vértice de origem até o vértice de destino usando o algoritmo de Bellman - Ford.

    Returns
        - caminho (List[int]): O caminho da origem até o destino no formato de uma lista de inteiros representando cada vértice.
        - custo (int): O custo total do caminho mínimo.
        - tempo (float): O tempo de execução do algoritmo em segundos.
    """

    start = time.time()

    dist = [float('inf')]*grafo.numVertices
    prev = [None] *grafo.numVertices

    dist[origem] = 0
    prev[origem] = 0

    for _ in range(grafo.numVertices - 1):
        atualizou = False
        for u in range(grafo.numVertices):
            for v, peso in grafo.vizinhos(u):
                if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    atualizou = True
        if not atualizou:
            break

    # Verificação de ciclos negativos
    for u in range(grafo.numVertices):
        for v, peso in grafo.vizinhos(u):
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                end = time.time()
                return None, float('-inf'), end - start

    end = time.time()

    caminho = []
    atual = destino

    while atual != origem:
        caminho.append(atual)
        atual = prev[atual]
        if atual is None:
            return None, float('inf'), end - start

    caminho.append(origem)
    caminho.reverse()

    return caminho, dist[destino], end - start

def caminhoMinFloydWarshall(grafo: ListaAdjacencias, origem: int, destino: int) -> Tuple[List[int], int, float]:
    """
    Calcula o caminho mínimo do vértice de origem até o vértice de destino usando o algoritmo de Floyd-Warshall.

    Returns:
        - caminho (List[int]): O caminho da origem até o destino no formato de uma lista de inteiros representando cada vértice.
        - custo (int): O custo total do caminho mínimo.
        - tempo (float): O tempo de execução do algoritmo em segundos.
    """

    start = time.time()

    dist = [[float('inf')] * grafo.numVertices for _ in range(grafo.numVertices)]
    prev = [[None] * grafo.numVertices for _ in range(grafo.numVertices)]

    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i == j:
                dist[i][j] = 0
                prev[i][j] = i
            else:
                for (v, peso) in grafo.vizinhos(i):
                    if v == j:  # v == j, existe aresta (i, j)
                        dist[i][j] = peso
                        prev[i][j] = i
                        break

    # Algoritmo principal
    for k in range(grafo.numVertices):
        for i in range(grafo.numVertices):
            for j in range(grafo.numVertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    end = time.time()
    caminho = []

    # Verificação de ciclos negativos
    if dist[origem][destino] == float('inf'):
        return None, float('-inf'), end - start

    # Construindo o caminho do destino até a origem
    else:
        atual = destino
        while atual != origem:
            caminho.append(atual)
            atual = prev[origem][atual]
            if atual is None:
                return None, float('inf'), end - start

        caminho.append(origem)
        caminho.reverse()

    return caminho, dist[origem][destino], end - start