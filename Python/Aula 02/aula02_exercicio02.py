# Ex 02. Crie um dicionário que armazene as idades de 5 pessoas (Já preenchido), 
# usando o nome como chave e a idade como valor. Então:
#     a. Adicione uma nova pessoa ao dicionário com seu respectivo nome e idade e exiba o dicionário atualizado.
#     b. Utilize um for para adicionar 3 novas pessoas ao invés de uma.

cadastro = {
    'Diego': 36,
    'Túlio': 26,
    'Daiana': 36,
    'Andréia': 45,
    'Fátima': 67
}
print('Cadastro atual:')
for nome, idade in cadastro.items():
    print(f'- {nome} => {idade} anos.')

# a. Adicione uma nova pessoa ao dicionário com seu respectivo nome e idade e exiba o dicionário atualizado.
cadastro['Adilio'] = 69
print('\nCadastro atualizado (a):')
for nome, idade in cadastro.items():
    print(f'- {nome} => {idade} anos.')
print()

# b. Utilize um for para adicionar 3 novas pessoas ao invés de uma.
for n in range(1, 3+1):
    nome = input(f'Digite o nome da {n}ª pessoa: ')
    idade = int(input(f'Digite a idade da {n}ª: '))
    cadastro[nome] = idade  # adicionando as novas pessoas ao dicionário
print('\nCadastro atualizado (b):')
for nome, idade in cadastro.items():
    print(f'- {nome} => {idade} anos.')
