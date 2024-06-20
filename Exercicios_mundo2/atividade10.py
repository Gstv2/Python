from random import *
import os

itens = ["pedra",'papel','tesoura','lagarto','spock']
computador = randint(0,5)


os.system("cls")
print()
jogador = int(input('''Escolha sua jogada
[ 1 ]Pedra
[ 2 ]Papel
[ 3 ]Tesoura
[ 4 ]Lagarto
[ 5 ]Spock
[ 6 ]TUTORIAL
sua escolha: '''))

jogador += -1

while(jogador > 4 or jogador < -1):
    os.system("cls")
    if jogador == 6:
        print('''
As regras de Pedra-papel-tesoura-lagarto-Spock são:

Tesoura corta papel
Papel cobre pedra
Pedra esmaga lagarto
Lagarto envenena Spock
Spock esmaga (ou derrete) tesoura
Tesoura decapita lagarto
Lagarto come papel
Papel refuta Spock
Spock vaporiza pedra
Pedra amassa tesoura


''')

    jogador = int(input('''Escolha sua jogada
[ 1 ]Pedra
[ 2 ]Papel
[ 3 ]Tesoura
[ 4 ]Lagarto
[ 5 ]Spock
[ 6 ]TUTORIAL
sua escolha: '''))
    
    
print('-=-'*10)
print('O jogador escolheu {} e o computador escolheu {}'.format(itens[jogador],itens[computador]))
print('-=-'*10)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 2:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 3:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 4:
        print('O computador PERDEU! e jogador GANHOU!')
        
        
elif computador == 1:
    if jogador == 0:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 3:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 4:
        print('jogador PERDEU! e o computador GANHOU!')
        
        
        
elif computador == 2:
    if jogador == 0:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 1:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 3:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 4:
        print('O computador PERDEU! e jogador GANHOU!')
        
        
        
        
elif computador == 3:
    if jogador == 0:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 1:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 2:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 3:
        print('EMPATE!')
    elif jogador == 4:
        print('jogador PERDEU! e o computador GANHOU!')
        
        
        
elif computador == 4:
    if jogador == 0:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 1:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 2:
        print('jogador PERDEU! e o computador GANHOU!')
    elif jogador == 3:
        print('O computador PERDEU! e jogador GANHOU!')
    elif jogador == 4:
        print('EMPATE!')


