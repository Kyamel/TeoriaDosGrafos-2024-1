import matrizAdjacencias
import listaAdjacencias

#criando um grafo representado por matriz de adjacencias:
grafo = matrizAdjacencias.MatrizAdjacencias(5)

#adicionando arestas:
grafo.addAresta(0,1)
grafo.addAresta(0,2)
grafo.addAresta(0,4)
grafo.addAresta(3,0)
grafo.addAresta(1, 4, 10)

#exibindo a matriz de adjacencias:
grafo.printGrafo()

#exibindo os vertices vizinhos de um determinado vertice:
print("Vizinhos de {}: {}".format(1, grafo.vizinhos(0)))
print("Vizinhos de {}: {}".format(1, grafo.vizinhos(1)))