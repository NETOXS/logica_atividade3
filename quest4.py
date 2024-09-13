def teste(a, b):
    soma = a + b
    if soma % 2 != 0:
        print(f"A soma de {a} (par) e {b} (ímpar) é {soma}, que é ímpar.")
    else:
        print(f"A soma de {a} e {b} é {soma}, que não é ímpar.")

# Teste
teste(2, 3)  # Saída esperada: ímpar 
teste(4, 4)  # Saída esperada: não ímpar