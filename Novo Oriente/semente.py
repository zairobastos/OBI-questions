def dias_fita(F, R, posicoes_gotas):
    # Inicializa a fita com todos os elementos iguais a 0
    fita = [0] * F
    
    # Preenche a fita com as gotas
    for gota in posicoes_gotas:
        fita[gota - 1] = 1

    # Inicializa o contador de dias
    dias = 0

    # Enquanto a fita não estiver tomada, continua a simulação
    while sum(fita) < F:
        # Inicializa a fita auxiliar
        fita_aux = [0] * F

        # Preenche a fita auxiliar com as gotas
        for i in range(F):
            if fita[i] == 1:
                fita_aux[i] = 1
                if i > 0:
                    fita_aux[i - 1] = 1
                if i < F - 1:
                    fita_aux[i + 1] = 1

        # Atualiza a fita
        fita = fita_aux

        # Incrementa o contador de dias
        dias += 1

    # Retorna o número de dias
    return dias

# Leitura da entrada
f, r = map(int, input().split())
posicoes_gotas = list(map(int, input().split()))

# Chamada da função e impressão do resultado
print(dias_fita(f, r, posicoes_gotas))
