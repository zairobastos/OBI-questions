n, m = map(int, input().split())

resp = 0  

for i in range(1, m + 1):
    resto = n - i  
    
    if 2 * m < resto:
        continue
    
    menor = max(1, resto - m)
    
    maior = min(resto - 1, m)
    
    resp += (maior - menor + 1)

print(resp)