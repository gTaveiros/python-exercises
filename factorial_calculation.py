def fatorial(numero):
  acum = 1
  for i in range(1, numero + 1):
    acum = acum * i
  return acum

N = int(input("Digite o valor de N : "))
K = int(input("Digite o valor de K : "))

fat = fatorial(N) / (fatorial(K) * (fatorial(N-K)))

print(fat)