import caminhoMinimo
import listaAdjacencias
import sys
import concurrent.futures

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

TIME_LIMIT = 600 # 10 min
def run_with_timeout(func, *args, timeout=TIME_LIMIT):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(func, *args)  # Submete a função
        try:
            return future.result(timeout=timeout)  # Espera o resultado
        except concurrent.futures.TimeoutError:
            return None, None, TIME_LIMIT  # Se ultrapassar o tempo, retorna valores padrão

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Numero invalido de parametros! Argumentos esperados: main.py grafo.txt origem(int) destino(int)")
        sys.exit(1)

    # sys.argv[1] contem o nome do arquivo a ser lido
    grafo = leitura(sys.argv[1])

    print("Processando...")
    print(50 * "-")

    algoritmos = {
        "Dijkstra": caminhoMinimo.caminhoMinDijkstra,
        "BellmanFord": caminhoMinimo.caminhoMinBellmanFord,
        "FloydWarshall": caminhoMinimo.caminhoMinFloydWarshall,
    }

    for nome, func in algoritmos.items():
        caminho, custo, tempo = run_with_timeout(func, grafo, int(sys.argv[2]), int(sys.argv[3]))
        print(f"Algorítimo:", nome)
        print("Caminho mínimo:", caminho)
        print("Custo:", custo)
        print(f"Tempo: {tempo:.3f}s")
        print(50 * "-")