'''Ex 03. Faça uma função "listar_nomes" que recebe uma lista de nomes e mostra todos os nomes no formato abaixo:
Dica: Utilize um For

Entrada: ["Marcos", "Gabriel", "Lidia"]

Nomes:
- Marcos
- Gabriel
- Lidia
'''

    # Definindo a função
def listar_nomes(nomes:list) -> str:
    'Essa função serve para mostrar os nomes cada um em uma linha'
    for nome in nomes:
        print(f' - {nome}')

nomes = []
cont = 's'

    # ENTRADA: Coletando os nomes pelo usuário:
while cont.lower() == 's':
    nome = input('Digite um nome: ')
    nomes.append(nome)
    cont = input('Você deseja digitar mais um nome (s/n)? ')

    # SAÍDA: Chamando a função para mostrar a lista de nomes
listar_nomes(nomes)