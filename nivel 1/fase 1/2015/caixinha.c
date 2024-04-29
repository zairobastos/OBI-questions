#include <stdio.h>

int main() {
    int n, m, resp = 0;
    scanf("%d %d", &n, &m);  // leio os valores de "n" e "m"

    // para cada uma das possíveis quantidades do primeiro amigo
    for (int i = 1; i <= m; i++) {
        int resto = n - i;  // vejo quantos palitos ainda sobram

        // se for impossível dividí-los entre os dois amigos restantes
        // dou continue e não faço mais nada nessa repetição
        if (2 * m < resto) {
            continue;
        }

        // menor será a menor quantidade que o segundo amigo pode ganhar
        int menor = (resto - m) > 1 ? (resto - m) : 1;

        // e maior será a maior quantidade
        int maior = (resto - 1) < m ? (resto - 1) : m;

        // como a quantidade do terceiro amigo já fica definida
        // adiciono a "resp" a quantidade de números no intervalo (menor, maior)
        resp += (maior - menor + 1);
    }

    // e por fim, imprimo o valor de "resp"
    printf("%d\n", resp);

    return 0;
}
