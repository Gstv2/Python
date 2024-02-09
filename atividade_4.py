import os 

os.system('cls')
print('Olá Mundo!!')

print('\n==== DESAFIO 22 Analisador de Textos ====') 
nome = str(input("digite seu nome: ")).strip()
print("Seu nome tudo MAISCULO {}".format(nome.upper()))
print("Seu nome tudo minusculo {}".format(nome.lower()))
Qt_nome = len(nome)-nome.count(' ')
print("Seu nome tem {} letras".format(Qt_nome))
Primeiro_nome = nome.split()
print("Seu Primeiro nome é {} e tem {} letras".format(Primeiro_nome[0], len(Primeiro_nome[0])))


print('\n==== DESAFIO 23 Separando Digitos ====') 
num = int(input("digite um numero entre 0 e 9999: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print("Analisando Numero...")
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))

print('\n==== DESAFIO 24 Conferindo se tem "Santos" ====') 
cidade = str(input("digite o nome da sua cidade: ")).strip()
print(cidade[:5].upper() == "SANTOS")

print('\n==== DESAFIO 25 Conferindo se tem "Santos" ====') 
nome = str(input("digite seu nome: ")).strip()
nome = nome.lower()
print("silva" in nome)

print('\n==== DESAFIO 26 Primeira e ultima ====') 
frase = str(input("digite seu nome: ")).upper()
print("Existe {} A nessa Frase".format(frase.count("A")))
print("Primeira letra A {} nessa Frase".format(frase.find("A")+1))
print("Ultima letra A {} nessa Frase".format(frase.rfind("A")+1))

print('\n==== DESAFIO 27 Primeiro e ultimo nome ====') 
nome = str(input("digite seu nome: ")).strip()
print("Muito Prazer te conhecer!!")
n = nome.split()
print("Primeiro nome é {}".format(nome[0]))
print("Ultimo nome é{}".format(nome[len(nome)-1]))
