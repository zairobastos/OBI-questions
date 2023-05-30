# Leitura dos dados de entrada
N, C, M = map(int, input().split())
carimbadas = set(map(int, input().split()))
compradas = set(map(int, input().split()))

# Cálculo das figurinhas carimbadas que faltam
faltam = len(carimbadas - compradas)

# Impressão do resultado
print(faltam)
