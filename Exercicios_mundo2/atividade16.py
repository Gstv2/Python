import os

os.system("cls")
primeiro_termo = int(input("primeiro termo:"))
razao = int(input("razão: "))
decimo_termo = primeiro_termo + (10-1)*razao


for i in range(primeiro_termo,decimo_termo,razao):
    print("{}".format(i),end=" ")
