def teste(a, b):
    produto = a * b
    if produto % 2 == 0:
        print(f"O produto de {a} e {b} é {produto}, que é par.")
    else:
        print(f"O produto de {a} e {b} não é par.")

# Teste
teste(2, 4)  # Saída esperada: par
teste(5, 3)  # Saída esperada: não par