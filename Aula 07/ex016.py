# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela consegue comprar
# cotação em 24/10/22: R$ 5.29
real = float(input('Quanto dinheiro você tem? '))
dol = real / 5.29
print('Com {} reais você consegue comprar {} dólares. T.T'.format(real, dol))
