N = 100

M = 34

for (1 - 35)

i = 1

resto = 100 - 1 = 99

verifica = 2*34 < 99 = 68 < 99 Sim

| i               |      resto      |    verifica    | Sim / Não |
| --------------- | :-------------: | :-------------: | :--------: |
| 2               |  100 - 2 = 98  |     68 < 98     |    Sim    |
| 3               |  100 - 3 = 97  |     68 < 97     |    Sim    |
| .<br />.<br />. | .<br />.<br />. | .<br />.<br />. |    Sim    |
| 31              |  100 - 31 = 69  |     68 < 69     |    Sim    |
| 32              |  100 - 32 = 68  |     68 < 68     |    Não    |

menor = max (1,68-34 = 34) = 34

maior = min (67,34) = 34

resp += 34 - 34 + 1 = 0 + 1 = 1

| i  | resto         | verifica | Sim / Não |
| -- | ------------- | -------- | :--------: |
| 33 | 100 - 33 = 67 | 68 < 67  |    Não    |
| 34 | 100 - 34 = 66 | 68 < 66  |    Não    |

menor = max(1, 67 - 34 = 33) = 33

maior = min(66,34) = 34

resp += 34 - 33 + 1 = 1 + 1 = 2 + 1 = 3


menor = max(1, 66 - 34 = 32) = 32

maior = min(65,34) = 34

resp += 34 - 32 + 1 = 2 + 1 = 3 + 3 = 6