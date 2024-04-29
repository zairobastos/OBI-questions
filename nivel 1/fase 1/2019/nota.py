b = int(input())
t = int(input())

trapezio = ((b + t) * 160)/2

valor = (160 * 160)/2

if trapezio == valor:
    print('0')
elif trapezio > valor:
    print('1')
else:
    print('2')

# https://neps.academy/br/exercise/465