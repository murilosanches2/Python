from math import sqrt, hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cato adjacente: "))
a = (co*co) + (ca*ca)
h = sqrt(a)
#h = (co**2 + ca**2) ** (1/2)
#h = hypot(co, ca) fórmula da hipotenusa utilizando hypot da biblioteca math
print("A hipotenusa vale: {:.2f}".format(h))

#cateto oposto, adjacente