palavras = ["casa", "lana", "carro", "cadeira",
            "paralelepipedo", "drywall", "extintor",
            "mesa"]

import random as rnd

palavra = palavras[rnd.randrange(0,len(palavras))]

quantidade_letras = len(palavra)

print("Palavra tem ", quantidade_letras , " letras")

contador = 0

lacertando = "".rjust(quantidade_letras ,"*")

print(lacertando)

while True:
  letra = input("Digite uma letra : ")

  acertou = False

  temp = ""

  for i in range(0,quantidade_letras):
    if (palavra[i] == letra):
      temp = temp + letra
      acertou = True
    else:
      temp = temp + lacertando[i]
  lacertando = temp

  if (contador == 6):
    print("Perdeu!")
    print("A palavra era :", palavra)
    break

  if (lacertando == palavra) or (letra == palavra):
    print("Acertou! Parabéns")
    break

  if (not acertou):
    print("Errou!")
    contador = contador + 1
    print("Erros :", contador)

  print(lacertando)