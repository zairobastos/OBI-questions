n, M = map(int, input().split())
mat = [[]] * (n+1)
vl = [0] * (n+1)
vc = [0] * (M+1)
m = {}
s = set()

for i in range(1, n+1):
    mat[i] = input().split()
    s.update(mat[i])
    vl[i] = int(input())

for i in range(1, M+1):
    vc[i] = int(input())

while len(m) < len(s):
    for i in range(1, n+1):
        qtd = 0
        summ = 0
        aux = ""
        ok = True

        for j in range(1, M+1):
            if mat[i][j] not in m:
                if qtd == 0:
                    qtd += 1
                    aux = mat[i][j]
                elif aux == mat[i][j]:
                    qtd += 1
                else:
                    ok = False
                    break
            elif mat[i][j] in m:
                summ += m[mat[i][j]]

        if ok and qtd > 0:
            m[aux] = (vl[i] - summ) // qtd

    for i in range(1, M+1):
        qtd = 0
        summ = 0
        aux = ""
        ok = True

        for j in range(1, n+1):
            if mat[j][i] not in m:
                if qtd == 0:
                    qtd += 1
                    aux = mat[j][i]
                elif aux == mat[j][i]:
                    qtd += 1
                else:
                    ok = False
                    break
            elif mat[j][i] in m:
                summ += m[mat[j][i]]

        if ok and qtd > 0:
            m[aux] = (vc[i] - summ) // qtd

for key, value in m.items():
    print(key, value)


""" 4 5
df bb cg df df 11
ee az cg az ee 6
df cg cg df df 10
az az cg az az 6
6 7 8 6 6 """
