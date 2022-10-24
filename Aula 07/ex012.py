# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = float(input('Digite um número: '))
dob = num * 2
tri = num * 3
sqrt = num ** (1/2)
print('Considerando o número {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(num, dob, tri, sqrt))
