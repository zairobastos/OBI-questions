def contar_numeros(S, A, B):
    if S < 1 or S > 36:
        raise ValueError("S deve estar entre 1 e 36")
    if A < 1 or A > 10000:
        raise ValueError("A deve estar entre 1 e 10000")
    if B < 1 or B > 10000:
        raise ValueError("B deve estar entre 1 e 10000")
    if B < A:
        raise ValueError("B deve ser maior que A")

    def soma_digitos(n):
        soma = 0
        while n > 0:
            soma += n % 10
            n //= 10
        return soma

    count = 0
    for i in range(A, B+1):
        if soma_digitos(i) == S:
            count += 1

    return count


print(contar_numeros(S=5, A=100, B=600))

"""
    550 % 10 = 0
    soma = 0
    550 // 10 = 55
    n = 55
    55 % 10 = 5
    soma = 5
    55 // 10 = 5
    n = 5
    5 % 10 = 5
    soma = 10
    5 // 10 = 0
"""
