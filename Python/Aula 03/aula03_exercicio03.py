# Ex 03. Faça um programa que peça uma quantidade indefinida de números e adicione-os em uma lista, a cada valor inserido pergunte se o usuário deseja continuar, depois mostre o maior e o menor numero digitado. 

# Criando uma lista vazia
numeros = []

# Predefinindo o valor da variável seguir
seguir = 's'

# Inserção de números pelo usuário
while seguir == 's':
    num = int(input('Digite um número: '))
    numeros.append(num)
    seguir = input('Você desejar continuar? (s/n) ')

# Predefinindo os valores das variáveis maior e menor com o primeiro número da lista
maior = numeros[0]
menor = numeros[0]

# Definindo o maior número
for i in range(len(numeros)):
    if numeros[i] > maior:  # verifica se cada nº digitado é maior q o anterior
        maior = numeros[i]  
    if numeros[i] < menor: # verifica se cada nº digitado é menor q o anterior
        menor = numeros[i]

print(f'A lista de números é: {numeros}')
print(f'O maior número da lista é: {maior}')
print(f'O menor número da lista é: {menor}')
