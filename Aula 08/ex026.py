# Faça um programa que leia um ângulo qualquer e mostre na tela os valores de seno, cosseno e tangente deste ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
rad = radians(ang)
print(f'O seno do ângulo {ang} vale {sin(rad)}, o cosseno vale {cos(rad)} e a tangente é {tan(rad)}.')
