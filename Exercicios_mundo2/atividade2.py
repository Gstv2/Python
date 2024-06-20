print("Bem-vindo a um conversor de bases")
num = int(input("digite um numero: "))
print("[ 1 ] base binaria")
print("[ 2 ] base octal")
print("[ 3 ] base hexadecimal")

opcao = int(input("Qual opção: "))
if(opcao == 1):
    print("{} convertido para binario é {}".format(num, bin(num)[2:]))
elif(opcao == 2):
    print("{} convertido para octal é {}".format(num, oct(num)[2:]))
elif(opcao == 3):
    print("{} convertido para hexadecimal é {}".format(num, hex(num)[2:]))
