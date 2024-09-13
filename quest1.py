import math

def teste(n):
    quadrado = pow(n,2)
    if quadrado % 2 != 0:
        print(f"O quadrado de {n} é ímpar, logo {n} é ímpar.")
    else:
        print(f"O quadrado de {n} é par.")

# Teste
teste(3)  # Saída esperada: ímpar
teste(4)  # Saída esperada: par