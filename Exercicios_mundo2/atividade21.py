import os 

os.system("cls")

maior = 0
tot = 0
media = 0

for pessoa in range(1,5):
    print('----{}°pessoa----'.format(pessoa))
    nome = input("nome: ")
    idade = int(input('idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    
    # Média na idade
    media += idade
    
    # verificando idade
    if pessoa == 1:
        maior = idade
    else:
        if idade < 20 and sexo == "F":
            tot += 1
        
        if idade > maior and sexo == "M":
            maior = idade
            velho = nome
                
            
            
print('A média da idade das pessoas é {}'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,velho))
print('São um total de {} mulheres com menos de 20 anos'.format(tot))
