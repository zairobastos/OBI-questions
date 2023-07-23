def transforma_entrada(array):
    return [int(valor) for valor in array.split(" ")]


entrada = str(input())
entrada_vetor = transforma_entrada(entrada)

valores_cartela = []


def intervalo_dos_valores(array):
    for valor in array:
        if valor > entrada_vetor[2] or valor < 1:
            return False
    return True


for cartela in range(0, entrada_vetor[0]):
    val = input()
    int_val = transforma_entrada(val)
    if len(int_val) == entrada_vetor[1]:
        if (intervalo_dos_valores(int_val)):
            valores_cartela.append(int_val)
        else:
            valores_cartela.append([])
    else:
        valores_cartela.append([])

sorteados = input()
array_sorteados = transforma_entrada(sorteados)

array_ganhadores = [0]*entrada_vetor[0]
resultado = []
for val_sorteado in array_sorteados:
    c = 0
    for cartela in valores_cartela:
        if val_sorteado in cartela:
            array_ganhadores[c] += 1
        c += 1
    if entrada_vetor[1] in array_ganhadores:
        for index, value in enumerate(array_ganhadores, start=1):
            if value == entrada_vetor[1]:
                resultado.append(str(index))
        break
print(' '.join(resultado))
