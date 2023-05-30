#include <stdio.h>

int main() {
    int n, m, pa, velho;
    
    scanf("%d", &n);
    scanf("%d", &m);
    
    pa = m - n;
    velho = m + pa;
    printf("%d", velho);
    return 0;
}