A = 4
B = A + 2
C = B - A
while A < 8:
  if C > 1:
    B = C + 1
    C = C - 1
    A = A + 2
  else:
    A = A + 1
    B = A + 3
  if B < 4:
    C = 5
    B = 3
print(A + B - C)