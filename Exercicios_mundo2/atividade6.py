from datetime import date

data_atual = date.today().year
ano_nascimento = int(input("Ano nascimento: "))

idade = data_atual - ano_nascimento
if idade <= 9:
    print("Sua classificação é MIRIM!")
elif 9 < idade <= 14:
    print("Sua classificação é INFANTIL!")
elif 14 < idade <= 19:
    print("Sua classificação é JUNIOR!")
elif 19 < idade <= 25:
    print("Sua classificação é SÊNIOR!")
else:
    print("Sua classificação é MASTER!")