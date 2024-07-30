from random import randint
num = randint(0, 5)
print('Tente adivinhar qual número estou pensando!')
chute = int(input("Digite um número entre 0 e 5: "))
if chute == num:
    print("Parabéns! o número que eu estava pensando era: {}".format(num))
else:
    print("Ops! Você errou =( o número que eu pensei era: {}".format(num))
