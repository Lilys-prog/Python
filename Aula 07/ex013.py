# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('O aluno teve as notas {} e {}, o que resultou em uma média de {:.1f}.'.format(nota1, nota2, media))



