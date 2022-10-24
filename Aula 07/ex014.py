# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
met = float(input('Quantos metros? '))
cent = met * 100
mil = met * 1000
print('{} metro(s) equivalem a {} centímetros e {} milímetros.'.format(met, cent, mil))
