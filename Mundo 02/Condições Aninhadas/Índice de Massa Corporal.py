KG = float(input("Digite o seu peso, em KG: "))
Alt = float(input("Digite sua altura, em M: "))
IMC = KG / (Alt * 2)
if IMC <= 18.5:
    print("Abaixo do peso!")
    print("Seu IMC é de: {:.2f}".format(IMC))
elif (IMC > 18.5) and (IMC <= 25):
    print("Peso ideal!")
    print("Seu IMC é de: {:.2f}".format(IMC))
elif (IMC > 25) and (IMC <= 30):
    print("Sobrepeso!")
    print("Seu IMC é de: {:.2f}".format(IMC))
elif (IMC > 30) and (IMC <= 40):
    print("Obesidade!")
    print("Seu IMC é de: {:.2f}".format(IMC))
elif IMC > 40:
    print("Obersidade mórbida!")
    print("Seu IMC é de: {:.2f}".format(IMC))
