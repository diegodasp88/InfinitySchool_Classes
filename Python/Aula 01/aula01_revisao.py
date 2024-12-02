# Programa para descobrir se o ano é bissexto

# Entrada
ano = int(input('Digite o ano: ')) # Casting: conversão do tipo da variável

# Processamento
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

#Saída
if bissexto:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
