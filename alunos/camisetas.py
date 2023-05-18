N = int(input())
T = input()
qp = T.count('1')
qm = T.count('2')
Tp = int(input())
Tm = int(input())
if Tp >=qp and Tm >= qm:
    print('S')
else:
    print('N')