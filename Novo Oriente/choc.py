n = int(input())
partes = map(int, input().split())

count = sum(partes) - n

print(count)


n = int(input())

partes = [int(x) for x in input().split()]

count = 0
for i in range(n):
    count += partes[i] - 1

print(count)