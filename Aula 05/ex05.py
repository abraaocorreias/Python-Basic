#Crie um programa que peça um número e mostre:
    #"Positivo" se o número for maior que 0;
    #"Negativo" se o número for menor que 0;
    #"Zero" se o número for igual a 0.
    
num = float(input("Digite aqui um número: "))

if num>0:
    print("POSITIVO")
elif num<0:
    print("NEGATIVO")
else:
    print("ZERO")