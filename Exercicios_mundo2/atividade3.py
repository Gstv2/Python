numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

if numero1>numero2:
    print("{} é maior do que {}".format(numero1,numero2))
elif numero1<numero2:
    print("{} é maior do que {}".format(numero2,numero1))
else:
    print("Não existe valor maior, sao iguais!")