# Solicita ao usuário um número inteiro e o armazena em 'n'.
n = int(input()) 

# Incrementa 'n' em 1. Agora 'n' é o próximo número inteiro ao que o usuário inseriu.
n += 1

""" 
Calcula o enésimo termo da progressão aritmética com primeiro termo 1 e razão 1.
Isso é feito pela fórmula an = a1 + (n - 1) * r, onde a1 é o primeiro termo, 'n' é o número de termos e 'r' é a razão.
"""
an = 1  + (n - 1) * 1  

"""
Calcula a soma dos 'n' primeiros termos da progressão aritmética.
A fórmula utilizada é a soma de uma PA: S = (n * (a1 + an)) / 2, onde 'n' é o número de termos, 'a1' é o primeiro termo e 'an' é o enésimo termo.
"""
pa = (n*(1 + an))/2  

print(int(pa))  # Imprime a soma dos 'n' primeiros termos da progressão aritmética como um número inteiro.