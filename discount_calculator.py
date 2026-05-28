def desconto_cliente(vp, vd):
  vp = vp - (vp * (vd / 100))
  return vp



preco = float(input("Digite o valor do produto :"))
desconto = float(input("Digite o valor de desconto :"))



print("O valor final do produto é" , desconto_cliente(preco, desconto))