def count_rectangles(N, K, sequence):
    count = 0  # Contador de retângulos com soma igual a K

    for i in range(N):
        curr_sum = 0  # Variável para armazenar a soma do subarray

        for j in range(i, N):
            curr_sum += sequence[j]  # Adiciona o próximo elemento ao subarray

            if curr_sum == K:  # Se a soma do subarray é igual a K, incrementa o contador
                count += 1

    return count


# Leitura dos dados de entrada
N, K = map(int, input().split())
sequence = list(map(int, input().split()))

# Chamada da função para contar os retângulos
num_rectangles = count_rectangles(N, K, sequence)

# Impressão do resultado
print(num_rectangles)
