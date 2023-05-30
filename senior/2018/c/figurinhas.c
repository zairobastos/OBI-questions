#include <stdio.h>

int main() {
    int N, C, M;
    scanf("%d %d %d", &N, &C, &M);

    int carimbadas[N];
    for (int i = 0; i < C; i++) {
        scanf("%d", &carimbadas[i]);
    }

    int compradas[M];
    for (int i = 0; i < M; i++) {
        scanf("%d", &compradas[i]);
    }

    // Cálculo das figurinhas carimbadas que faltam
    int faltam = 0;
    for (int i = 0; i < C; i++) {
        int carimbada = carimbadas[i];
        int encontrada = 0;
        for (int j = 0; j < M; j++) {
            if (compradas[j] == carimbada) {
                encontrada = 1;
                break;
            }
        }
        if (!encontrada) {
            faltam++;
        }
    }

    // Impressão do resultado
    printf("%d\n", faltam);

    return 0;
}
