#Crie uma função que recebe um número e retorne se ele é par ou ímpar.

def paridade(a):
    if a%2 == 0:
        return(f"O valor {a} é um número par.")
    else:
        return(f"O valor {a} é um número ímpar.")
num = int(input('Digite aqui um número inteiro: '))
print(paridade(num))