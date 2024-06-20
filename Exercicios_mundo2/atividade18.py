import os

os.system("cls")
print("Dectetor de Palídromo!")
frase = input("digite um frase: ").strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''


for i in range(len(junto) -1, -1, -1):
    inverso += junto[i]
print('{}, {}'.format(junto,inverso))
if inverso == junto:
    print("Essa frase é um palindromo!")
else:
    print("Essa frase não é um palindromo!")