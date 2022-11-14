# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela somente a sua porção inteira
import math
from math import trunc
num = float(input('Digite um número real: '))
n = math.trunc(num)
print(n)

