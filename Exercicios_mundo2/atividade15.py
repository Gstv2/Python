import os

os.system("cls")
resultado = 0
for i in range(1,7):
    num = int(input("digite um numero: "))
    if num % 2 == 0:
        resultado += num
        
print("A soma dos numeros pares digitado foi {}".format(resultado))