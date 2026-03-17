idade = int(input("Digite sua idade: "))

if idade <12:
    print("criança")
elif idade <18:
    print("Adolescente")
elif idade <60:
    print("Adulto")
else: 
    print("idoso")