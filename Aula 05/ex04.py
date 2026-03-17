#Crie um programa que peça a nota do aluno (0 a 10) e mostre:
    #Aprovado se a nota >=7
    #Recuperação se a nota >=5 e <7
    #Reprovado se nota <5.
    
nota = float(input("Digite aqui a sua nota: "))

if nota <5:
    print("Você está REPROVADO!")
elif nota <7:
    print("Você está em RECUPERAÇÃO!")
else:
    print("Você está APROVADO")