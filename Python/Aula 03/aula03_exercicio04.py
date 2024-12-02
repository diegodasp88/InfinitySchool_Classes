# Ex 04. Faça um programa que peça um numero e mostre o enésimo termo da sequencia de fibonacci. 
# Exemplo:
# >>> Até qual termo deseja mostrar? 8
# 0 1 1 2 3 5 8 13

num = int(input('Até qual termo deseja mostrar? '))

fibo = 0
ant = 1
ant2 = 0

for i in range(0, num):
    if i <= 1:
        print(fibo)
        fibo += 1
    else:
        fibo = ant + ant2
        print(fibo)
        ant2 = ant
        ant = fibo
    