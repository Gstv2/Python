from datetime import date

data_atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = data_atual - ano

if idade == 18:
    print("Esta na hora de se alistar!!!!")
elif idade > 18:
    print("Você rapido, era para ter se alistado a {} anos".format(idade-18))
else:
    print("Ainda nn esta na hora de se alistar, falta {} anos".format((idade-18)*-1))