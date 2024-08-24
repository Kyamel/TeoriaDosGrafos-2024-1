from listaAdjacencias import ListaAdjacencias

# retorna a densidade do grafo:
def densidade(grafo):
    return grafo.numArestas / (grafo.numVertices * (grafo.numVertices - 1))

# retorna o complemento do grafo:
def complemento(grafo):
    complemento = ListaAdjacencias(grafo.numVertices)
    # complemento = matrizAdjacencias.MatrizAdjacencias(grafo.numVertices)

    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i != j and not grafo.possuiAresta(i, j):
                complemento.addAresta(i, j)
    
    return complemento

# retorna True se o grafo eh completo:
def completo(grafo):
    for i in range(grafo.numVertices):
        for j in range(grafo.numVertices):
            if i != j and not grafo.possuiAresta(i, j):
                return False
    return True

# retorna True se o grafo eh regular:
def regular(grafo):
    grau = grafo.grau(0)
    for i in range(1, grafo.numVertices):
        if grau != grafo.grau(i):
            return False
    return True

