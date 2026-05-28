peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em centímetros: "))

altura = altura / 100

imc = peso / (altura ** 2)

print("O seu IMC é:", imc)