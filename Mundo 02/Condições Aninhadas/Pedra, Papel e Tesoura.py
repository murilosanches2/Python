from random import choice
pessoa = int(input('''Jokenpô!!\n[1] Pedra\n[2] Papel\n[3] Tesoura\n'''))
numeros = [1, 2, 3]
computador = choice(numeros)
if pessoa == 1 and computador == 1:
    print("Nós dois escolhemos pedra! Empate!!")
elif pessoa == 1 and computador == 2:
    print("Você escolheu pedra e eu papel! Você perdeu!!")
elif pessoa == 1 and computador == 3:
    print("Você escolheu pedra e eu tesoura! Você ganhou!!")
elif pessoa == 2 and computador == 1:
    print("Você escolheu papel e eu pedra! Você ganhou!!")
elif pessoa == 2 and computador == 2:
    print("Nós dois escolhemos papel! Empate!!")
elif pessoa == 2 and computador == 3:
    print("Você escolheu papel e eu tesoura! Você perdeu!!")
elif pessoa == 3 and computador == 1:
    print("Você escolheu tesoura e eu pedra! Você perdeu!!")
elif pessoa == 3 and computador == 2:
    print("Você escolheu tesoura e eu papel! Você ganhou!!")
elif pessoa == 3 and computador == 3:
    print("Nós dois escolhemos tesoura! Empate!")
