import listaAdjacencias
import sys
import mst

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
    if len(sys.argv) != 3:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt limite_grau")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])
    if mst.is_direcionado(grafo):
        print("Erro: O grafo é direcionado! Este algoritmo só funciona para grafos não-direcionados.")
        sys.exit(1)

    print("Grafo:")
    grafo.printGrafo()

    try:
        arvore = mst.degree_limited_mst(grafo, int(sys.argv[2]))
        print("Arvore Geradora mínima com limite de grau:")
        arvore.printGrafo()
    except Exception as e:
        print("Erro:", e)