import os


os.system('cls')
print('Olá Mundo!!')

print('\n==== DESAFIO 5 antecessor, sucessor ====') 

num = int(input('digite um numero: '))
print('o antecessor é {} e o sucessor {} do numero {}'.format(num-1, num+1, num))

print('\n==== DESAFIO 6 Dobro, triplo, raiz ====')

num = int(input('digite outro numero: '))
print('seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(num*2, num*3, num**(1/2)))

print('\n==== DESAFIO 7 Média ====')

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1+nota2)/2

print('primeira nota {} e a segunda nota {}'.format(nota1, nota2))
print('A media desse aluno é {:.1f}'.format(media))

print('\n==== DESAFIO 8 Medidas(cm, mm) ====')
num = float(input('digite outro numero: '))
print('{} metros em cm é {:.0f}cm e em mm é {:.0f}mm'.format(num, num*100, num*1000))

print('\n==== DESAFIO 9 Tabuada ====')
num = int(input('digite outro numero: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))


print('\n==== DESAFIO 10 Conversor de Moeda ====')
real = float(input('Quanto dinheiro voçê tem na carteira?: '))

dolar = real / 3.27

print('Com {} voçê consegui {:.2f} dolares'.format(real, dolar))

print('\n==== DESAFIO 11 Pintando Parede ====')

largura = float(input('digite a largura: '))
altura = float(input('digite a altura: '))

Area = largura*altura
print('A area dessa parede com a largura {}m e altura {}m é {:.2f}m²'.format(largura, altura, Area))
print('O pintor vai precisar de {:.1f}l de tinta para essa parede'.format(Area/2))


print('\n==== DESAFIO 12 Desconto ====')

Preço = float(input('digite o preço do produto: '))

Total = Preço - Preço*0.05
print('O valor {} com o desconto de 5% fica {:.1f}'.format(Preço, Total))

print('\n==== DESAFIO 13 Aumento ====')

Salário = float(input('digite o valor do seu Salário: '))

Total = Salário + Salário*0.15
print('O salário de {} com o aumento de 15% fica {:.1f}'.format(Salário, Total))

print('\n==== DESAFIO 14 Conversor de temperatura ====')

C = int(input('digite a temperatura em C: '))

F = (C * 9/5) + 32
print('A temperatura era de {}C convertido fica {}F'.format(C, F))

print('\n==== DESAFIO 15 Aluguel de carros ====')

Dia_Alugado = int(input('quantos dias o carro foi alugado '))
Km_rodado = float(input('Quantos Km foi andado: '))

Total = (Dia_Alugado*60)+(Km_rodado*0.15)
print('O total do aluguel a pagar pelo carro é {:.2f} '.format(Total))



