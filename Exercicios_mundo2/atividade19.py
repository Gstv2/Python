from datetime import *

atual = date.today().year
totMaior = 0
totmenor = 0

for pess in range(1,8):
    nasc = int(input("em que ano a {}° pessoa nasceu: ".format(pess)))
    idade = atual-nasc
    if idade >= 21:
        totMaior += 1
    else:
        totmenor += 1

print('{}: de maiores\n{}: de menores'.format(totMaior,totmenor))
    