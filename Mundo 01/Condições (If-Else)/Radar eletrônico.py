velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print("Você foi multado!! O total da multa é R${:.2f}!".format(multa))
else:
    print("Velocidade dentro da via!")
