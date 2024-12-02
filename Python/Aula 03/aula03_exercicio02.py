# Ex 02. Faça um programa para pedir modelo, ano, preço fip e kilometragem de um carro (uso). Depois, calcule o preço final do carro a partir da kilometragem:
# - Km maior que 300_000, - 50%
# - Km maior que 200_000, - 35%
# - Km maior que 150_000, - 30%
# - Km maior que 100_000, - 20%
# - Outros Km             - 15%

# Pré definindo a variável preço
preco = 0

# Inserção de valores pelo usuário
modelo = input('Digite o modelo do carro: ')
ano = int(input('Digite o ano do carro: '))
fip = float(input('Digite o preço fit do carro: '))
uso = int(input('Digite a kilomnetragem do carro: '))

# Calculando o preço final do carro
if uso <= 100_000:
    preco = fip - (fip * (15/100))
elif uso <= 150_000:
    preco = fip - (fip * (20/100))
elif uso <= 200_000:
    preco = fip - (fip * (30/100))
elif uso <= 300_000:
    preco = fip - (fip * (35/100))
else:
    preco = fip - (fip * (50/100))

# Mostrando o valor
print(f'O preço final do carro é R$ {preco:.2f}')