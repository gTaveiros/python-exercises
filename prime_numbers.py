while True:
    numero = int(input("Digite um número : "))
    
    if 1 <= numero <= 10000:
        break

for a in range(2, numero + 1):
    primo = True

    for i in range(2, a):
        if a % i == 0:
            primo = False
            break

    if primo:
        print("Número primo:", a)