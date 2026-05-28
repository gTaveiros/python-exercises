def fatorial(numero):
  acum = 1
  for i in range(1, numero + 1):
    acum = acum * i
  return acum

while True:
  numero =int(input("Digite um número :"))
  if (numero >= 1) and (numero <=100):
    break
print("Fatorial de ", numero, "é", fatorial(numero))
