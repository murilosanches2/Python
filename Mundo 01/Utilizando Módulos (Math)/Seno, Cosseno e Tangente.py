from math import radians, sin, cos, tan
x = float(input("Insira um ângulo: "))
seno = sin(radians(x))
coss = cos(radians(x))
tang = tan(radians(x))
print("O ângulo de {} tem o SENO de {:.2f}".format(x, seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(x, coss))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(x, tang))
