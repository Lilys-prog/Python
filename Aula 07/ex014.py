# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
met = float(input('Quantos metros? '))
cent = met * 100
mil = met * 1000
print('{}m equivalem a {}cm e {}mm.'.format(met, cent, mil))
