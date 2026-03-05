# Crie um programa que some os números de 1 até 5 usnado while e no final mostre o resultado.

numero = 1
soma = 0
while numero <= 5:
    soma += numero
    numero += 1
    print(f"A soma dos números de 1 a {numero-1} é: {soma}")