# Peça o peso (kg) e a altura (m) do usuário e calcule o IMC.
a = float(input("Digite o seu peso(kg): "))
b = float(input("Digite a sua altura(m): "))
imc = (a/(b**2))   
print(f"Você digitou {a} kg e {b} m")
print(f"O seu IMC é {imc:.2f}") 