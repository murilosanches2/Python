km = float(input("Insira em KM, a distância da sua viagem: "))
if km <= 200:
    preço = km * 0.5
    print("O preço da sua viagem vai custar: R${:.2f}".format(preço))
else:
    preço = km * 0.45
    print("O preço da sua viagem vai custar: R${:.2f}".format(preço))
