c = 0
for i in range(0,6):
    entrada = input()
    if entrada == 'V':
        c+=1

if c>=5 and c<=6:
    print(1)
elif c>=3 and c<=4:
    print(2)
elif c>=1 and c<=2:
    print(3)
else:
    print(-1)
