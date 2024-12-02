# Ex 01. Faça um programa que peça: nome e 3 notas de um aluno, depois armazene no dicionário as seguintes informações:
# - nome
# - notas (lista)
# - media
# - situacao ('APROVADO' se maior que 6, se não, 'REPROVADO')
# Depois mostre as informações do aluno na tela.

aluno = {}
notas = []

# Nome
aluno['nome'] = input('Digite o nome do aluno: ')

# Notas
for i in range(1, 3+1):
    nota = float(input(f'Digite a {i}ª nota do aluno: '))
    notas.append(nota)
    aluno['notas'] = notas

# Média
aluno['media'] = sum(aluno.get('notas')) / len(aluno.get('notas'))

# Situação
if aluno.get('media') > 6:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'

# Mostrar na tela
print()
print('INFORMAÇÕES DO ALUNO:')
print(f'Nome: {aluno.get('nome')}')
print(f'Notas: {aluno.get('notas')}')
print(f'Média: {aluno.get('media'):.2f}')
print(f'Situação: {aluno.get('situacao')}')
