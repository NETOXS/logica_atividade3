def teste(a, b):
    produto = a * b
    if produto % 2 != 0:
        print(f"O produto de {a} e {b} é {produto}, que é ímpar.")
    else:
        print(f"O produto de {a} e {b} é {produto}, não é ímpar.")

# Teste
teste(3, 5)  # Saída esperada: ímpar
teste(3, 4)  # Saída esperada: não ímpar