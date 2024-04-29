def calcular_peso_subarvore(grafo, no):
    """
    Função recursiva para calcular o peso da subárvore enraizada em 'no'.
    Retorna o peso da subárvore.
    """
    n = len(grafo[no])
    if n == 0:
        return 1  # Nó folha tem peso 1
    
    peso = calcular_peso_subarvore(grafo, grafo[no][0])
    for i in range(1, n):
        if calcular_peso_subarvore(grafo, grafo[no][i]) != peso:
            return -1  # Se pesos diferentes, retorna -1
    return n * peso  # Retorna o peso total da subárvore

def main():
    N = int(input("Digite o número de arestas: "))
    
    grafo = [[] for _ in range(N + 1)]  # Lista de adjacências do grafo
    
    for _ in range(N):
        u, v = map(int, input().split())
        grafo[v].append(u)  # Adiciona a aresta v->u
    
    peso_total = calcular_peso_subarvore(grafo, 0)
    if peso_total > 0:
        print("bem")  # Se todos os pesos são iguais, árvore é bem formada
    else:
        print("mal")  # Se algum peso é diferente, árvore é mal formada

if __name__ == "__main__":
    main()
