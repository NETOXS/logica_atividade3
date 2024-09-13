def teste(a, b, c):
    if b % a == 0 and c % b == 0:
        print(f"{a} divide {b}, {b} divide {c}, então {a} divide {c}.")
    else:
        print(f"Não é verdade que {a} divide {c}.")

# Teste
teste(2, 4, 8)  # Saída esperada: a divide c
teste(3, 6, 10)  # Saída esperada: a não divide c