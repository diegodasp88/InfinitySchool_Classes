# Ex 01. Faça um programa que peça 3 numeros e informe o maior e o menor.

# Inserção de valores pelo usuário
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

# Pré definindo os valores maiores e menores
maior = num1
menor = num3

# Encontrando o valor maior:
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

# Encontrando o valor menor:
if num2 < num3 and num2 < num1:
    menor = num2
elif num1 < num3 and num1 < num2:
    menor = num1

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')