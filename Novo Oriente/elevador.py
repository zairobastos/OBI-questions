n, c = map(int, input().split())

resposta = 'N'
for i in range(n):
    s, e = map(int, input().split())
    c += s - e
    if c < 0:
        resposta = 'S'


if resposta == 'S':
    print('S')
else:
    print('N')