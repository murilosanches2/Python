l = float(input("Em metros, digite a largura da parede: "))
a = float(input("Em metros, digite a altura da parede: "))
area = a * l
tinta = area / 2
print("A área da sua parede é {:.3}m² e precisará de {:.3} litros de tinta!".format(area, tinta))
