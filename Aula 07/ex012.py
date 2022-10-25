# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = float(input('Digite um número: '))
dob = num * 2
tri = num * 3
sqrt = num ** (1/2)
print('Considerando o número {},\nseu dobro é {},\nseu triplo é {}\ne sua raiz quadrada é {:.2f}.'.format(num, dob, tri, sqrt))
