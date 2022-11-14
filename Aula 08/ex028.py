# O professor quer sortear a ordem de apresentação de trabalho de seus 4 alunos. Faça um programa que leia os nomes dos 4 e mostre a ordem sorteada.
import random
alunos = ('Juliana', 'Paulo', 'Gustavo', 'Jasielle')
lista = random.sample((alunos), 4)
print(lista)




