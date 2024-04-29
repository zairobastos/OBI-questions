MAX = 1000
pos = [0] * MAX

def main():
    posicoes, pastas = map(int, input("Digite o número de posições e pastas: ").split())

    # Limpando o vetor de posições
    for i in range(posicoes):
        pos[i] = 0
    print(pos)
    # Lendo as etiquetas das pastas
    etiquetas = list(map(int, input("Digite as etiquetas das pastas: ").split()))
    for numero in etiquetas:
        print(numero)
        pos[numero - 1] += 1
        print(pos)

    # Verificando se o padrão se aplica
    maximo = pos[0]
    salto = 0
    ok = True

    for i in range(1, posicoes):
        if pos[i] != maximo:
            if pos[i] == maximo - 1 and not salto:
                maximo -= 1
                salto = 1
            else:
                ok = False
                break

    if ok:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
