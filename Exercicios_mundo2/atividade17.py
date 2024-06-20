import os

os.system("cls")

numero = int(input("digite um numero: "))
tot = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[33m", end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print("{}".format(i),end=" ")
print("\n\033[m0 O número {} foi divido {} vezes".format(numero,tot))
if tot == 2:
    print('Esse número é PRIMO!!')
else:
    print('Esse número NÂO é primo')
