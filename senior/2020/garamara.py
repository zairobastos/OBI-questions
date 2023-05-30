def is_anagram_curinga(word1, word2):
    if len(word1) != len(word2):
        return False

    for c in word2:
        if c != '*' and c not in word1:
            return False

    return True


# Leitura das palavras de entrada
P = input()
A = input()

# Verifica se A é um anagrama curinga de P
if is_anagram_curinga(P, A):
    print("S")
else:
    print("N")
