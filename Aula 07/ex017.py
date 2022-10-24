# Faça um programa que leia a altura e a largura de um parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
alt = float(input('Altura (em metros): '))
lar = float(input('Largura (em metros): '))
area = alt * lar
tinta = area / 2
print('Para pintar uma parede de {}m² são necessários {} litros de tinta.'.format(area, tinta))


