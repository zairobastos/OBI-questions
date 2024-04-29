n = int(input())
a,b,c,d,e,f,g = map(int, input().split())

a = a - d - e
b = b - d - f
c = c - e - f

n -= a + b + c+ d + e + f + g

if n < 0:
    print("S")
else:
    print("N")
