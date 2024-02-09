import random
import time
import os 
from datetime import date

os.system('cls')

print('\n==== DESAFIO 28 Jogo de advinhar ====')

print('-=-'*20)
print('Vamos jogar um jogo de adivinhação?')
sim = input('Sim/Não ')
print('-=-'*20)
capitalizado = sim.capitalize()
if capitalizado == 'Sim':
    print('Ok, vou vou pensar em um número de 0 a 5, e você tem que acertar!')
elif capitalizado == 'Não':
    print('Ahh, que pena! Se você quiser jogar, é só voltar mais tarde!')
computador = random.randint(0, 5)

# Escolhe o número
jogador = int(input('Agora é sua hora de adivinhar! Escreva um número de 0 a 5, e tente adivinhar o número que eu pensei! '))
print('Processando...')
time.sleep(3)
if jogador == computador:
    print('Poxa, você me venceu! Quer jogar de novo?')
else:
    print('Eu ganhei! Vamos jogar de novo?')





print('\n==== DESAFIO 29 Limite de Velocidade 80km ====')

km = int(input("Qual a sua velocidade atual? "))
if km <= 80:
    print("Dirija com segurança!!")
if km > 80:
    multa = (km - 80) * 7
    print("MULTADOO!! voçê passou da velocidade limite voçê foi multado em {}".format(multa))



print('\n==== DESAFIO 30 IMPAR OU PAR ====')

num = int(input("Digite um numero: "))
resultado = num % 2
if resultado == 0:
    print("esse numero é PAR")
elif resultado == 1:
    print("esse numero é IMPAR")




print('\n==== DESAFIO 31 Viajem ====')

km = int(input("Qual a distancia da sua viajem atual? "))
if km <= 200:
    passagem = km * 0.5
    print("Sua passagem custará R${}".format(passagem))
if km > 200:
    passagem = km * 0.45
    print("Sua passagem custará R${}".format(passagem))

    
print('\n==== DESAFIO 32 Bissexto ====')
ano = int(input("Qual ano quer analisar?? Digite 0 para analisar o ano atual!: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO!!".format(ano))
else:
    print("O ano {} Não é BISSEXTO!!".format(ano))


print('\n==== DESAFIO 33 < ou > ====')
a = int(input('O primeiro numero: '))
b = int(input('O segundo numero: '))
c = int(input('O Terceiro numero: '))
#verificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#verificando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

#verificando se sao iguais
if a == b and b == c:
    print("todos os numero sao iguais")
else: 
    print("O maior numero digitado foi {} e o menor foi {}".format(maior, menor))



print('\n==== DESAFIO 34 salario ====')

salario = int(input("Qual o seu salario atual? "))
if salario > 1250:
    novo = (salario * 0.10) + salario
    print("Sue salario agr é de {} ele era de {}, teve um aumento de 10%".format(salario, novo))
if salario <= 1250:
    novo = (salario * 0.15) + salario
    print("Sue salario agr é de {} ele era de {}, teve um aumento de 15%".format(salario, novo))


print('\n==== DESAFIO 35 Analisando Triangulos ====')

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Os segmentos acima PODEM FORMAR UM TRIANGULO!!!")
else:
    print("Os segmentos acima NAO PODEM FORMAR UM TRIANGULO!!!")
