# Ex. 01. Faça uma função "multiplicar" que recebe dois números e retorna o produto entre eles.

# Definindo a função
def mult(n1, n2):
    return n1 * n2

# Pedindo o usuário para definir os parâmetros
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

# Printando o resultado para o usuário
print(f'O produto desses números é {mult(num1, num2)}.')