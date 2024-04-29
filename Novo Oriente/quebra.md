MAXN = 200200 

Definimos ele nesse tamanho porque uma das restrições é que o tamanho do vetor seja 200000

lista = [None] * MAXN

Crio uma lista vazia para armazenar os valores que iremos receber

n = int(input()) - Recebemos o valor correspondente a quantidade de peças que iremos ter na nossa lista.

Então pq não fazemos apenas: lista = [None] * n ao invés de lista = [None] * MAXN. Não podemos fazer dessa maneira pq o "n" ele corresponde a quantidade de peças que iremos ter na lista e não a última posição da última peça que teremos na lista.


Em seguida, faço um for que vai de 1 até n+1.

Conteúdo do FOR: e, c, d = map(str, input().split())

por debaixo dos panos o que essa linha tá fazendo.

Suponha que a sua entrada seja: "5 A 1"

O input() recebe a entrada "5 A 1", o input().split() gera um array ["5", "A", "1"]

map(str,input().split()) = map(str,["5", "A", "1"])

sendo assim o map ele vai mapear os valores desse array, por exemplo

| array                                  | é string          | variavel |
| -------------------------------------- | ------------------ | -------- |
| [***"5"***, "A", "1"]          | "5" é string? Sim | e = "5"  |
| [~~"5"~~,***"A"***, "1"]      | "A" é string? Sim | c = "A"  |
| [~~"5"~~,~~"A"~~, ***"1"***] | "1" é string? Sim | d = "1"  |

próximo passo

transformar os valores das variáveis "e" e "d" em inteiros, para isso temos:
e = int(e) = 5

d = int(d) = 1

se a gente der um print na lista o que a gente vai ter: [None, None, Nome,...,None]

em lista[e] = (c,d) => lista[5] = ("A",1)


**Mas porque utilizar uma tupla e não um array, pois a tupla ela permite ter diferente tipos de conteúdos dentro dela, diferentemente do array. E a sua forma de acessar o seu conteúdo é semelhante a um array.**

Então a nossa lista fica da seguinte forma, após a primeira inserção:

Na posição 5 do array, teremos ("A",1)

[None, None, Nome, None, ("A",1),...,None]

E ASSIM SUCESSIVAMENTE.


agora definimos o prox = 0. Pq igual a 0, pois no enunciado da questão diz que sem o array começa na posição 0 e finaliza quando chegar na posição 1

por isso que o nosso While vai rodar enquanto o valor de prox for diferente de 1

e o conteúdo do print é o seguinte, a gente está printando o valor da posição 0 da tupla que são as letras.

pegando o caso "5 A 1"

quando o próximo for igual a 5, ele printará a letra A e em seguida atualiza o valor do prox para 1


Teste de mesa:

| entrada | c | e | d | lista[e] =(c,d)    |                                lista                                |
| ------- | - | - | - | ------------------ | :------------------------------------------------------------------: |
| 5 A 1   | A | 5 | 1 | lista[5] = ("A",1) |        [None, None, None, None, None, ("A",1), None,...,None]        |
| 0 T 7   | T | 0 | 7 | lista[0] = ("T",7) |      [("T",7), None, None, None, None, ("A",1), None,...,None]      |
| 3 M 5   | M | 3 | 5 | lista[5] = ("M",5) |    [("T",7), None, None, ('M",5), None, ("A",1), None,...,None]    |
| 7 E 3   | E | 7 | 3 | lista[7] = ("E",3) | [("T",7), None, None, ('M",5), None, ("A",1), None,("E",3)...,None] |


AGORA VAMOS PERCORRER A LISTA:

[("T",7), None, None, ('M",5), None, ("A",1), None,("E",3)...,None]

prox = 0

|  prox  | lista       | print | continua               |
| :----: | ----------- | ----- | ---------------------- |
| 0 != 1 | lista[0][0] | T     | prox = lista[0][1] = 7 |
| 7 != 1 | lista[0][7] | TE    | prox = lista[7][1] = 3 |
| 3 != 1 | lista[0][3] | TEM   | prox = lista[3][1] = 5 |
| 5 != 1 | lista[0][5] | TEMA  | prox = lista[0][5] = 1 |
| 1 = 1 |             |       |                        |
