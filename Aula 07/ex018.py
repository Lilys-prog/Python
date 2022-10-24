# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Qual o preço original do produto? '))
desc = preco - preco * 0.05
print('O produto com o preço original de {} reais sai por {} reais, na promoção.'.format(preco, desc))


