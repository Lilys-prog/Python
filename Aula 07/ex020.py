# Escreva um programa que converte uma temperatura em ºC para ºF.
cel = float(input('Qual a temperatura em ºC? '))
fah = (cel * 9 / 5) + 32
print('Se a temperatura em celsius é {:.1f}ºC, em fahrenheit é {:.1f}ºF.'.format(cel, fah))