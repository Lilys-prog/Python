# O professor quer sortear a ordem de apresentação de trabalho de seus 4 alunos. Faça um programa que leia os nomes dos 4 e mostre a ordem sorteada.
from random import sample
alunos = ('Juliana', 'Paulo', 'Gustavo', 'Jasielle')
lista = sample((alunos), 4)
print(lista)
#-------------------------------------------------------
# coisas que o Guanabara fez diferente.
# ele tb pediu os nomes como input, eu ia fazer e esqueci, whatever.
# usou o método 'shuffle' do módulo random



