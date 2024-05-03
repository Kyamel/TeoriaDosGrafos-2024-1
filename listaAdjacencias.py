# Representacao computacional de um grafo por meio de lista de adjacencias:
class ListaAdjacencias:
    # inicializa o grafo:    
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.numArestas = 0
        # inicializa a lista de adjacencias:
        self.lista = [[] for _ in range(numVertices)]

    # retorna a ordem do grafo:
    def ordem(self):
        self.numVertices
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        self.numArestas

    # adiciona uma aresta (v1, v2) no grafo:
    # peso eh um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        self.lista[v1].append((v2, peso))
        self.numArestas += 1

    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        for (i,p) in self.lista[v1]:
            if i == v2:
                return True
        return False
    
    # retorna uma lista com os vizinhos de v:
    def vizinhos(self, v):
        return self.lista[v]

    # retorna o grau de um vertice:
    def grau(self, v):
        return len(self.lista[v])

    # printa o grafo no formato de lista de adjacencias:
    def printGrafo(self):
        for i in range(self.numVertices):
            print("Vertice {}: {}".format(i, self.lista[i]))