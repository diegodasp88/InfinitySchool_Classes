# S E T S
    # Conjuntos matemáticos
        # Não são ordenados, elementos aparecem aleatŕios
        # Se número, o print ordena
        # Não contém elementos duplicados (se houver ele corta)

conjunto = {1, 2, 3, 4, 3, 0}
print(conjunto)


# Operações
a = {'A', 'B', 'C'}
b = {'D', 'A', 'E'}
print(f'Conjunto a: {a}')
print(f'Conjunto b: {b}')

    # União
print(f'União de conjuntos "a" e "b" {a.union(b)}')
'''Elementos duplicados são mesclados.'''

    # Intersecção
print(f'Intersecção dos conjuntos "a" e "b": {a.intersection(b)}')
'''Quando não houver, retorna conjunto vazio "set()"'''


# Removendo duplicados de uma lista
nomes = ['Lidia', 'Rafael', 'Caio', 'Caio', 'Lidia'] #lista
print(nomes)

nomes_sem_duplicados = list(set(nomes))
'''Ao transformar uma lista em conjunto, ele automaticamente retira os duplicados.'''

# Ordenando o conjunto:
nomes_sem_duplicados.sort()

print(nomes_sem_duplicados)

print()
print('---------------------------------------------------------------------')
print()

# D I C I O N Á R I O S
    # Chaves vazias são interpretadas como dicionários
    # Os itens são ordenados

aluno = {
    'matricula': '12345',   # Item 1
    'nome': 'Diego',        # Item 2
    'curso': 'Programação', # Item 3
    'notas': [8, 10, 9.5]
}
print(aluno)


# Acessando valores:
print(f'Matrícula: {aluno['matricula']}') 
'''Se a chave não existir, SEU CÓDIGO QUEBRA'''

print(f'Nome: {aluno.get('nome')}')
'''Se a chave não existir, retorna None'''

print(aluno.get('nao_existe')) # retorna None
print(aluno.get('nao_existe', 'Chave não encontrada')) # retorna 'Chave não encontrada'


# Criando / Atualizando chaves
    
    # Atualizando chave
aluno['matricula'] = '54321'

    # Criando chave
aluno['media'] = sum(aluno.get('notas')) / len(aluno.get('notas'))

print(aluno)

    # Removendo chave
if 'situacao' in aluno: # Verificando se existe a chave a ser excluída
    aluno.pop('situacao') # Excluindo a chave

    # Atualizar dicionário
aluno.update({
    'nome': 'Diego DASP',
    'situacao': 'APROVADO'
})
print(f'Dicionário após atualizações: {aluno}')

