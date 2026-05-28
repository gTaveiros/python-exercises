A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))
C = int(input("Digite o valor de C:"))
if (A > B):
  X = A
  A = B
  B = X
if (B > C):
  X = B
  B = C
  C = X
if (A > B):
  X = A
  A = B
  B = X
if (B > C):
  X = B
  B = C
  C = X
print(" O menor é ", A, " O maior é ", C)