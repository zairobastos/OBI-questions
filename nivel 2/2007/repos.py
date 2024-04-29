MAX = 11000

class Pacote:
    def __init__(self, id, versao, instalada):
        self.id = id
        self.versao = versao
        self.instalada = instalada

def compara(a, b):
    if b.id - a.id:
        return a.id - b.id
    elif b.versao - a.versao:
        return b.versao - a.versao
    else:
        return b.instalada - a.instalada

p = [None] * MAX

if __name__ == "__main__":
    c, n = map(int, input().split())

    for i in range(c):
        id, versao = map(int, input().split())
        p[i] = Pacote(id, versao, 1)

    for i in range(c, n + c):
        id, versao = map(int, input().split())
        p[i] = Pacote(id, versao, 0)

    p.sort(key=lambda x: (x.id, x.versao, -x.instalada))

    lid = -1

    for pacote in p:
        if lid != pacote.id and not pacote.instalada:
            print(pacote.id, pacote.versao)
        lid = pacote.id
