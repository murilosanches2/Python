print("\033[7;32mOlá, mundo!\033[m")
print("\033[1;31;47mOlá, mundo!\033[m")
print("\033[1;32;41mOlá, mundo!\033[m")
cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "amarelo":"\033[33m",
         "pretoebranco":"\033[7m"}
nome = "Murilo"
print("Olá! Muito prazer em te conhecer, {}{}{}!!".format("\033[4;34m",nome,"\033[m"))
print("Olá! Muito prazer em te conhecer, {}{}{}!!".format(cores["amarelo"],nome,cores["limpa"]))
print("Olá! Muito prazer em te conhecer, {}{}{}!!".format(cores["pretoebranco"],nome,cores["limpa"]))