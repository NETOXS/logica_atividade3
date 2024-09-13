def teste(a, b):
    soma = a + b
    if soma % 2 == 0:
        print(f"A soma de {a} e {b} é {soma}, que é par.")
    else:
        print(f"A soma de {a} e {b} é {soma}, que não é par.")

# Teste
teste(2, 4)  # Saída esperada: par
teste(2, 3)  # Saída esperada: não par