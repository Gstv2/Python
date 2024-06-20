r1 = float(input("primeiro segmento: "))
r2 = float(input("segunda segmento: "))
r3 = float(input("terceira segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triangulo")
    if r1 == r2 and r2 == r3:
        print("É um triangulo EQUILATERO!")
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print("É um triangulo ISOCELES!")
    else:
        print("É um triangulo ESCALENO!")
else:
    print("OS segmentos não podem formar um triangulo")
    
