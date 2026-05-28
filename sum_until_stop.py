acumulado = 0
sair = 1
while sair == 1:
  numero = int(input("Digite um número : (negativo para parar) "))
  if numero > 0:
    acumulado = acumulado + numero
  else:
     sair = 0
print("O resultado é: ", acumulado)