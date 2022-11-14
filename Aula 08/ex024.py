# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela somente a sua porção inteira
from math import trunc
num = float(input('Digite um número real: '))
n =  trunc(num)
print(n)
# ----------------------------------------
# outras resoluções possíveis dadas pelo Guanabara
# usando o math.floor
# usando a função interna "int(num)", que vai retornar só o inteiro mesmo, essa nem precisa importar nada

