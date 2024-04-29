#include <stdio.h>

int main() {
    int b, t;
    scanf("%d", &b);
    scanf("%d", &t);

    int trapezio = ((b + t) * 160) / 2;
    int valor = (160 * 160) / 2;

    if (trapezio == valor) {
        printf("0\n");
    } else if (trapezio > valor) {
        printf("1\n");
    } else {
        printf("2\n");
    }

    return 0;
}
