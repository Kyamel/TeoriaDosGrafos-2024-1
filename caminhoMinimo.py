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
        for v in O:
            if dist[v] < menor:
                menor = dist[v]
                u = v
        
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
            return None, float('inf')
        
    caminho.append(origem)
    caminho.reverse()
    
    return caminho, dist[destino], end - start

def caminhoMinFloydWarshall(grafo: ListaAdjacencias, origem: int, destino: int) -> Tuple[List[int], int, float]:
    pass

def caminhoMinBellmanFord(grafo: ListaAdjacencias, origem: int, destino: int) -> Tuple[List[int], int, float]:
    pass