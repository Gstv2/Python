peso = float(input("digite seu peso [kg]: "))
altura = float(input("digite sua altura [cm]: "))

imc = peso/(altura**2)

if imc < 18.5:
    print("Voçê esta abaixo do peso!")
elif 18.5 <= imc < 25:
    print("Voçê esta no peso ideal!")
elif 25 <= imc < 30:
    print("Voçê esta sobrepeso!")
elif 30 <= imc < 40:
    print("Voçê esta OBESIDADE!")
else:
    print("Voçê esta OBESIDADE MRBIDA!")                             