import math
import os
import random

os.system('cls')
print('Olá Mundo!!')

print('\n==== DESAFIO 16 Quebrando um Numero ====') 

num = float(input('digite um número: '))
print (f'a parte inteira de {num} é {math.trunc (num)}')

print('\n==== DESAFIO 17 Cateto e hipotenusa ====') 

co = float(input("digite o valor do cateto oposto: "))
ca = float(input("digite o valor do cateto adjacente: "))
hi = math.hypot(co, ca)
print("Seu CO é {}, seu CA é {} e sua Hipotenusa {:.2f}".format(co,ca,hi))

print('\n==== DESAFIO 18 Sen, Cos e Tan ====') 

num = float(input("digite outro numero: "))
Cos = math.cos(math.radians(num))
sin = math.sin(math.radians(num))
tan = math.tan(math.radians(num))
print("Seu COSSENO é {:.2f}\nseu SENO é {:.2f}\ne sua TANGENTE {:.2f}".format(Cos,sin,tan))


print('\n==== DESAFIO 19 Sorteando um item de uma lista ====') 
n1 = str(input("digite o nome do Primeiro aluno: "))
n2 = str(input("digite o nome do Segundo aluno: "))
n3 = str(input("digite o nome do Terceiro aluno: "))
n4 = str(input("digite o nome do Quarto aluno: "))

lista = [n1,n2,n3,n4]
print(lista)
print(random.choice(lista))

print('\n==== DESAFIO 20 Sorteando uma ordem de item de uma lista ====') 
n1 = str(input("digite o nome do Primeiro aluno: "))
n2 = str(input("digite o nome do Segundo aluno: "))
n3 = str(input("digite o nome do Terceiro aluno: "))
n4 = str(input("digite o nome do Quarto aluno: "))

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(lista)




