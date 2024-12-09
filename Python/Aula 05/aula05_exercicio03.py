'''Ex 03. Faça uma função "listar_nomes" que recebe uma lista de nomes e mostra todos os nomes no formato abaixo:
Dica: Utilize um For

Entrada: ["Marcos", "Gabriel", "Lidia"]

Nomes:
- Marcos
- Gabriel
- Lidia
'''

nomes = []

# Definindo a função de listar
def listar_nomes(nomes: list):
    print('Nomes: ')
    for nome in nomes:
        print(f'- {nome}')

# Definindo a função de adicionar
def adicionar_nome(dados: list):
    nome = input('Digite o nome: ')
    dados.append(nome)

# Menu
while True:
    print(' Armazenador de Nomes '.center(30, '-'))
    print('[1] - Listar Nomes')
    print('[2] - Adicionar novo Nome')
    print('[3] - Sair')
    print('-' * 30)

    opcao = input('Digite uma opção: ')

# Acessando as opções
    if opcao == '1':
        listar_nomes(nomes)
    elif opcao == '2':
        adicionar_nome(nomes)
    elif opcao == '3':
        print('Saindo do programa...')
        break
    else:
        print('Opção Inválida. Digite Novamente.')

print('Fim do Programa.')
