# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
cat1 = int(input('Digite o cateto oposto: '))
cat2 = int(input('Digite o cateto adjacente: '))
hip = sqrt(cat1 ** 2 + cat2 ** 2)
print(f'Neste triângulo, a hipotenusa vale {hip:.2f}.')
#----------------------------------------
# outras formas que o Guanabara fez:
# elevar a 1/2, pra fazer a sqrt
# importar o "math.hypot(cat1, cat2)", que já vai dar a hipotenusa





