cartas = str(input())
p, c, u, e = [], [], [], []
c2 = 2
for letra in cartas:
    if letra == 'P':
        concatena = cartas[c2-2]+cartas[c2-1]
        p.append(concatena)
        c2 += 3
    if letra == 'E':
        concatena = cartas[c2-2]+cartas[c2-1]
        e.append(concatena)
        c2 += 3
    if letra == 'U':
        concatena = cartas[c2-2]+cartas[c2-1]
        u.append(concatena)
        c2 += 3
    if letra == 'C':
        concatena = cartas[c2-2]+cartas[c2-1]
        c.append(concatena)
        c2 += 3


def verifica_duplicados(array):
    for x in array:
        if array.count(x) > 1:
            return True
    return False


array_global = [c, e, u, p]

for i in array_global:
    if verifica_duplicados(i):
        print("erro")
    else:
        tam = len(i)
        print(13-tam)
