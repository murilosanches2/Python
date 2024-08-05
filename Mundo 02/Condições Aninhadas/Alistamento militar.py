pessoa = int(input("Insire em que ano você nasceu: "))
idade = 2024 - pessoa
if idade < 18:
    tempo = 18 - idade
    print("Você irá se alistar daqui {} ano(s)!".format(tempo))
elif idade == 18:
    print("Você está na idade certa para se alistar!")
else:
    tempo = idade - 18
    print("Você está {} ano(s) atrasado(s) com o serviço militar!".format(tempo))
