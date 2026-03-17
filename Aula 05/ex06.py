#Crie um programa que peça números ao usuário e vá somando. O programa deve repetir usando while até o usuário digitar 0.
    #Regras:
        #Se o número for positivo, somar e mostrar "Número positivo adicionado";
        #Se o número for negativo, não somar e mostrar "Número negativo ignorado"
        #Se o número for 0, encerrar e mostrar a soma no final.

soma = 0

while num !=0:
    num = float(input("Digite aqui um número: "))
    
    if num >0:
        soma += num
        print(f"Número positivo adicionado e a soma é {soma}")
    elif num <0:
        print("Número negativo ignorado")
    else:
        print("Encerrando ...")
    break

print(f"Soma final é: {soma}")