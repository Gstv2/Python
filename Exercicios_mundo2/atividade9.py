print(20*"-=")
print("BEM VINDO AO PAGAMENTO")
print(20*"-=")

preco = float(input("Preço das compras: R$"))
print("""Qual forma de pagamento:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão""")

opcao = int(input("Qual opção: "))
if opcao == 1:
    print("ficou {:.2f} com odesconto".format(preco - 10/100))
if opcao == 2:
    print("ficou {:.2f} com o desconto".format(preco - 5/100))
if opcao == 3:
    print("ficou {:.2f} SEM JUROS".format(preco))
if opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input("quantas parcelas: "))
    parcela = total/totalparc
    print("ficou {}x de R${:.2f}, total {:.2f} COM JUROS".format(totalparc,parcela,total))
else:
    print("OPCAO INVALIDA!!!")
