#include <stdio.h>

int count_rectangles(int N, int K, int sequence[]) {
    int count = 0;  // Contador de retângulos com soma igual a K

    for (int i = 0; i < N; i++) {
        int curr_sum = 0;  // Variável para armazenar a soma do subarray

        for (int j = i; j < N; j++) {
            curr_sum += sequence[j];  // Adiciona o próximo elemento ao subarray

            if (curr_sum == K) {  // Se a soma do subarray é igual a K, incrementa o contador
                count++;
            }
        }
    }

    return count;
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    int sequence[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &sequence[i]);
    }

    // Chamada da função para contar os retângulos
    int num_rectangles = count_rectangles(N, K, sequence);

    // Impressão do resultado
    printf("%d\n", num_rectangles);

    return 0;
}
