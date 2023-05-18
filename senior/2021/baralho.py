cartas = str(input())

def lista_cartas(entrada):
    return [entrada[i:i+3] for i in range(0,len(entrada),3)]

array_de_cartas = lista_cartas(entrada=cartas)
c, e, u, p = [], [], [], []

for posicao in array_de_cartas:
    if posicao[2] == 'C':
        c.append(posicao)
    elif posicao[2] == 'E':
        e.append(posicao)
    elif posicao[2] == 'U':
        u.append(posicao)
    elif posicao[2] == 'P':
        p.append(posicao)

def verifica_duplicados(array):
    for x in array:
        if array.count(x) > 1:
            return True
    return False

array_global = [c,e,u,p]

for i in array_global:
    if verifica_duplicados(i):
        print("erro")
    else:
        tam = len(i)
        print(13-tam)