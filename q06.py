def find_third_num(A, B):
    if A < 1 or A > 1000000000:
        raise ValueError("A deve estar entre 1 e 1000000000")
    if B < 1 or B > 1000000000:
        raise ValueError("B deve estar entre 1 e 1000000000")
    if B < A:
        raise ValueError("B deve ser maior que A")

    C = 2*A-B
    return C


print(find_third_num(A=1, B=1000000000))
