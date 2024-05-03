import matrizAdjacencias
import listaAdjacencias
import info

# criando um grafo:
# grafo = listaAdjacencias.ListaAdjacencias(6)
grafo = matrizAdjacencias.MatrizAdjacencias(6)


# adicionando arestas:
grafo.addAresta(0,1)
grafo.addAresta(0,2)
grafo.addAresta(0,4)
grafo.addAresta(3,0)
grafo.addAresta(1, 4, 10)

# exibindo as listas de adjacencias:
grafo.printGrafo()

# exibindo os vertices vizinhos de um determinado vertice:
print("Vizinhos de {}: {}".format(0, grafo.vizinhos(0)))
print("Vizinhos de {}: {}".format(1, grafo.vizinhos(1)))

# exibindo o grau de um vertice:
print("Grau do vertice {}: {}".format(0, grafo.grau(0)))

# testando se existe uma aresta (1, 2) no grafo:
print("Existe aresta (1, 2) no grafo? {}".format(grafo.possuiAresta(1, 2)));