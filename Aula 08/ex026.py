# Faça um programa que leia um ângulo qualquer e mostre na tela os valores de seno, cosseno e tangente deste ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
rad = radians(ang)
print(f'O seno do ângulo {ang} vale {sin(rad):.1f}, o cosseno vale {cos(rad):.1f} e a tangente é {tan(rad):.1f}.')
#---------------------------------------------------
# outras formas que o Guanabara fez
# tudo igual, não usou outra forma
