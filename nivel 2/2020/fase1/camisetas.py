num_premiado = int(input())
tam_premiado = str(input())

def transforma_entrada(array):
    return [int(valor) for valor in array.split(" ")]

qtd_pequenas = int(input())
qtd_media = int(input())

roupas = transforma_entrada(tam_premiado)
qtd_p,qtd_m =0, 0
for peca in roupas:
    if peca == 1:
        qtd_p+=1
    if peca == 2:
        qtd_m+=1

if (qtd_m <= qtd_media) and (qtd_p<=qtd_pequenas):
    print("S")
else:
    print('N')