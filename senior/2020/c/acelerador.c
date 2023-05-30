#include <stdio.h>

int main() {
    int distancia_total, distancia_emissor_acelerador, circunferencia_acelerador;
    int distancia_acelerador, num_voltas_completas, posicao_final_acelerador, sensor_atingido;
    
    scanf("%d", &distancia_total);
    
    distancia_emissor_acelerador = 3;
    circunferencia_acelerador = 8;
    
    distancia_acelerador = distancia_total - distancia_emissor_acelerador;
    num_voltas_completas = distancia_acelerador / circunferencia_acelerador;
    
    posicao_final_acelerador = distancia_acelerador % circunferencia_acelerador;
    sensor_atingido = posicao_final_acelerador % 3 + 1;
    
    printf("%d\n", sensor_atingido);
    
    return 0;
}
