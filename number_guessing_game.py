# importar as bibliotecas
import random as rnd



for i in range(1, 3 + 1):
  # sortear um número
  sorteado = rnd.randrange(1,10+1)
  numero = int(input("Digite um número de 1 a 10 :"))

  if (numero == sorteado):
    print("Acertou!")
    break
  else:
    print("Errou")
    print("O número sorteado era :", sorteado)

