# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
dist = float(input('Quantos quilômetros foram percorridos? '))
tempo = int(input('Por quantos dias o carro foi alugado? '))
pTempo = tempo * 60
pDist = dist * 0.15
print('O preço total a pagar é de {:.2f} reais.'.format(pTempo + pDist))

