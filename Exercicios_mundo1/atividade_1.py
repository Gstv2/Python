import os

print('Olá Mundo!!')

print('digite seu nome:')
nome_user = input('>>')

os.system('cls')
print('==== DESAFIO 1 ====')

print(20*'=')
print('olá {}!! Prazer em te conhecer'.format(nome_user))
print(20*'=')

print('==== DESAFIO 2 ====')

dia = input("Que dia do mês em que nasceu?")
mes = input("Em que mês você nasceu?")
ano = input("Por fim, Em que ano você nasceu?")
print ("Você nasceu no dia {} de {} de {}".format(dia,mes,ano))

print('==== DESAFIO 3 ====')

print('Calculadora de adição entre dois numeros:')
x = input("Digite o primeiro numero: ")
y = input("Agora digite o segundo numero: ")
x = int(x)
y = int(y)
soma = x + y
print("seu numero final é", soma)

print('==== DESAFIO 4 ====')

print('digite algo:')
valor = input('>>')

print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizado? {valor.istitle()}')