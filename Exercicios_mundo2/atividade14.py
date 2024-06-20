import os 

os.system("cls")
n = int(input("digite o numero que vc quer ver a tabuada: "))
for i in range(1,11):
    print( "{} x {} = {}".format(n,i,i*n))