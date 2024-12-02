# Lista
    # Estrutura ordenada e indexada de forma posicional

# Índices:  0      1    2    3
lista = ['Diego', 5.1, 90, True]

# Acessar valores:
print(lista[0]) # 'Diego'
print(lista[2]) # 90

# Adicionar valores:
lista.append() # Adicioina o valor entre parênteses ná última posição da lista.
lista.insert(2, 'DASP') # Adiciona valores numa posiçao específica: (índice, valor).

# Excluir valores:
lista.pop() # Excluir o ultimo elemento da lista.
lista.pop(0) # Excluir o elemento do indice específico. No caso, do índice 0.

# Tamanho da lista:
len(lista) # Retorna um valor referente a quantidade de elementos na lista.

# Somar os elementos da lista:
sum(lista)


# Utilização das listas:
nomes = []

    # 1 - Preencher:
for i in range(3):
    nome = input(f'Digite o nome do {i}º participante: ')
    nomes.append(nome)

    # 2 - Percorrer:
for nome in nomes:
    print(f'- {nome}')


# Procurar informação:
    #Exemplo: Existe o nome 'Diego' na lista?
existe = False
for busca in lista:
    if busca == 'Diego':
        existe = True
        break
if existe:
    print('O nome existe na lista.')
else:
    print('O nome nao existe na lista.')
