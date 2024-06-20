import os 

os.system("cls")
resultado = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        resultado += i
        cont += 1
print("A soma dos {} números solicitados é de {}".format(cont,resultado))