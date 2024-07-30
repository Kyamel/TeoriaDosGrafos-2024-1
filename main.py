import matrizAdjacencias
import listaAdjacencias
import info
import sys
import busca

# cria um grafo a partir de um arquivo:
def leitura(nomeArquivo):
    arquivo = open(nomeArquivo)

    str = arquivo.readline()
    str = str.split(" ")
    numVertices = int(str[0])
    numArestas = int(str[1])

    grafo = listaAdjacencias.ListaAdjacencias(numVertices)
    # grafo = matrizAdjacencias.MatrizAdjacencias(numVertices)

    for i in range(numArestas):
        str = arquivo.readline()
        str = str.split(" ")
        origem = int(str[0])
        destino = int(str[1])
        peso = int(str[2])
        grafo.addAresta(origem, destino, peso)

    return grafo

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])

    print(f"Densidade do grafo: {info.densidade(grafo)}")

    print("Grafo original:")
    grafo.printGrafo()
    print()

    complemento = info.complemento(grafo)
    print("Complemento:")
    complemento.printGrafo()
    print()

    print(f'Grafo eh completo? {info.completo(grafo)}')
    print(f'Grafo eh regular? {info.regular(grafo)}')

    print(f"DFS recursivo: {busca.dfsRecursivo(grafo, 0)}")
    print(f"DFS recursivo: {busca.dfsIterativo(grafo, 0)}")
    print(f"BFS: {busca.bfs(grafo, 0)}")
    