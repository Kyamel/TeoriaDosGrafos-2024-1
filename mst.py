import listaAdjacencias as la

def is_direcionado(graph: la.ListaAdjacencias) -> bool:
    for v1 in range(graph.numVertices):
        for (v2, _) in graph.vizinhos(v1):
            # Se não existir a aresta inversa (v2, v1), o grafo é direcionado
            if not graph.possuiAresta(v2, v1):
                return True  # É direcionado
    return False  # Não é direcionado

def degree_limited_mst(graph: la.ListaAdjacencias, grau_limite: int) -> la.ListaAdjacencias:
    # Ordena as arestas do grafo pelo peso (menor para maior) - princípio do Kruskal
    vertices = []
    for v1 in range(graph.numVertices):
        for (v2, peso) in graph.vizinhos(v1):
            vertices.append((v1, v2, peso))

    vertices = sorted(vertices, key=lambda x: x[2])  # Ordena as arestas pelo peso

    # Cria uma nova lista de adjacências para representar a árvore geradora mínima (MST)
    mst = la.ListaAdjacencias(graph.numVertices)

    # Inicializa o grau de cada nó em 0
    degraus = {node: 0 for node in range(graph.numVertices)}

    # Adiciona as arestas mantendo a restrição de grau
    for v1, v2, peso in vertices:
        # Verifica se ambos os nós ainda não excederam o limite de grau
        if degraus[v1] < grau_limite and degraus[v2] < grau_limite:
            mst.addAresta(v1, v2, peso)
            degraus[v1] += 1
            degraus[v2] += 1

        # Se já conectamos todos os nós, saímos do laço
        if mst.numArestas == graph.numVertices - 1:
            break

    # Se a árvore geradora não conseguiu conectar todos os nós
    if mst.numArestas != graph.numVertices - 1:
        raise Exception(f"Não foi possível conectar todos os vértices com o limite de grau: {grau_limite}.")

    return mst