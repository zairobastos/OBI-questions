#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    n += 1;

    int an = 1 + (n - 1) * 1;
    int pa = (n * (1 + an)) / 2;

    printf("%d\n", pa);

    return 0;
}
