entrada = input()
dados = entrada.split(" ")
dados = [int(x) for x in dados]

matriz = []
for i in range(0, dados[0]):
    valor = input()
    matriz.append(valor)


def iniciaMudanca():
    if int(matriz[0][0]) <= dados[1]:
        return True
    return False


aux_matriz = []
if iniciaMudanca():
    for linha in matriz:
        array = []
        for c in linha:
            if (int(c) <= dados[1]):
                array.append(1)
            else:
                array.append(0)
        aux_matriz.append(array)
    for linha in aux_matriz:
        for c in range(linha):
            if (c == 0):
                if (linha[c] == 1):
                    matriz[linha][c] == '*'
                if (linha[c+1] == 1):
                    matriz[linha][c+1] == '*'
                if (aux_matriz[linha+1][c] == 1):
                    aux_matriz[linha+1][c] == '*'
else:
    for i in matriz:
        print(i)
