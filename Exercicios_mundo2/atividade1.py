#Programa para aprovar empréstimo


valor_casa = float(input("Quanto é o valor da casa: "))
salario = float(input("Qual seu salário atual: "))
anos = int(input("Quantos anos deseja pagar: "))
minimo = 30/100 * salario

parcelas = valor_casa/(anos*12)
print("Para pagar uma cada de {:.2f} em {}, as parcelas será de R${:.2f}".format(valor_casa,anos,parcelas))

if parcelas <= minimo:
    print("Emprestimo concedido!")
else:
    print("Emprestimo NEGADO!!!")


