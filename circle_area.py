def calcular_area_circulo(raio):
    area = 3.141592 * (raio ** 2)
    return area

def main():
    raio = float(input("Digite o valor do raio do cŕiculo em R:"))
    area = calcular_area_circulo(raio)
    print("A área do círculo é:", area)

if __name__ == "__main__":
    main()