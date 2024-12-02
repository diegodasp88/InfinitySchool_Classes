# Exercício 01: Crie uma lista com 5 elementos de um tema a sua escolha.
    # a) Mostre na tela o elemento no índice 3.
    # b) Mostre na tela o 3º elemento da lista.
    # c) Mostre na tela o 1º elemento da lista.
'''
lista = ['Diego', 36, '02/11', 1.8, '80kg']
print(f'O elemento de índice 3 da lista é {lista[3]}')
print(f'O 3º elemento da lista é {lista[2]}')
print(f'O 1º elemento da lista é {lista[0]}')
'''

# Exercício 02: Faça um programa que peça 5 números e armazene-os em uma lista,
    # ao final mostre a lista na tela.
'''
numeros = []

for i in range(1, 5+1):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)

print(numeros)
'''

# Exercício 03: Faça um programa que peça o nome e 3 notas de um aluno, 
    # e armazene as notas em uma lista "notas", 
    # depois calcule a média do aluno utilizando as funções "sum" e "len".
'''
nome = input('Digite o nome do aluno: ')
notas = []

for j in range(1, 3+1):
    nota = float(input(f'Digite a {j}ª nota do aluno {nome}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'A média do aluno {nome} é {media:.2f}')
'''

# Exercício 04: Faça um programa que peça 6 numeros, 
    # e armazene-os em duas listas: "pares" e "impares". Depois mostre-as na tela.
'''
pares = []
impares = []

for k in range(1, 6+1):
    num = int(input(f'Digite o {k}º número: '))
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é {impares}')
'''
