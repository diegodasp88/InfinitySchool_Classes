# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
lista = []
for i in range(1,5+1):
    n = int(input(f'Digite o {i}º número: '))
    lista.append(n)
print(lista)
'''


# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
lista = []
for i in range(1,10+1):
    n = int(input(f'Digite o {i}º número: '))
    lista.append(n)
print(lista[::-1])
'''


# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
notas = []
for i in range(1,4+1):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f'A média entre as notas {notas} é {media:.2f}.')
'''


# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
frase = input('Digite uma frase: ').lower()
consoante = 0
for letra in frase:
    if letra in 'aeiou':
        consoante += 1
print(f'Na frase "{frase}" há {consoante} consoantes.')
'''


# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
pares = []
impares = []

for i in range(1,20+1):
    num = int(input(f'Digite o {i}º de 20 números: '))
    numeros.append(num)
    if num != 0:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

print(f'Lista de números digitados: {numeros}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')
