# Desafio: Faça um programa que peça 2 numeros,
    # depois armazene em uma lista "primos" todos os numeros 
    # primos entre os numeros informados (eles inclusos.)

from math import sqrt

inicio = int(input('Digite o número inicial do intervalo: '))
fim = int(input('Digite o número final do intervalo: '))
primos = []

for numero in range(inicio, fim + 1):
    eh_primo = True     # todos são primos até que prove o contrário
    
    for divisor in range(2, int(sqrt(numero)) + 1):
        if numero % divisor == 0:
            eh_primo = False    # se tem divisor: não é primo
            break
    
    if eh_primo and numero > 1:     # tem que ser maior que 1
        primos.append(numero)

print(f'Os números primos entre o intervalo sâo: {primos}')