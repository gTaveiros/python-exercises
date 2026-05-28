A=4
B=7
C=6
D=2
F=7
G=9
if C!=6:
   G=D+B
if (not(G==4))and(not(B>5)):
   if B!=6:
      G=G-A
G=G-C
if (D!=6)or(not(A>4)):
   B=G*B
   if A<5:
      A=C*C
   else:
      G=C*B
else:
   if (C!=9)or(B<=8):
      C=C*F
   else:
      A=B*F
   G=B*B
C=B*C
print(G+F+B-A)