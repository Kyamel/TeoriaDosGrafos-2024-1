import listaAdjacencias
import matrizAdjacencias

# versao recursiva do DFS (Aula 07 - slide 7):

def dfsRecursivo(grafo, u):
    R = []
    visitado = [False] * grafo.numVertices
    dfsRecursivoAux(grafo, R, visitado, u)
    return R

def dfsRecursivoAux(grafo, R, visitado, u):
    print(u)
    visitado[u] = True  # Marca o vértice atual como visitado
    R.append(u)  # Adiciona o vértice à lista de resultado
    
    # Percorre todos os vértices adjacentes
    for v in grafo.vizinhos(u):  
        if visitado[v[0]] ==  False:
            dfsRecursivoAux(grafo, R, visitado, v[0])


# versao iterativa do DFS (Aula 07 - slide 8):
def dfsIterativo(grafo, u):
    R = []
    pilha = []
    visitado = [False] * grafo.numVertices
    pilha.append(u)
    visitado[u] = True
    while len(pilha) > 0:
        u = pilha.pop()
        R.append(u)
        for v in grafo.vizinhos(u):
            if not visitado[v[0]]:
                pilha.append(v[0])
                visitado[v[0]] = True
    return R

# BFS (Aula 07 - slide 15):
def bfs(grafo, u):
    R = []
    fila = []
    visitado = [False] * grafo.numVertices
    fila.append(u)
    visitado[u] = True
    while len(fila) > 0:
        u = fila.pop(0) # pop 0 para simular fila
        R.append(u)
        for v in grafo.vizinhos(u):
            if not visitado[v[0]]:
                visitado[v[0]] = True
                fila.append(v[0])
    return R
