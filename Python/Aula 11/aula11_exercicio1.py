# Exercício 01: Criem uma Classe "Celular" que deve conter as propriedades:
# marca , modelo, cor
    # a. Crie um objeto da classe "Celular"
    # b. Mostre a marca e o modelo desse celular
    # c. Crie outro objeto da classe "Celular"
    # d. Mostre a marca e a cor desse outro celular.

# Criando a classe
class Celular:
    def __init__(self, marca: str, modelo: str, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
# a. Crie um objeto da classe "Celular"
celular1 = Celular('Xiami', 'Poco X5 Pro', 'Azul')

# b. Mostre a marca e o modelo desse celular
print(f'Marca: {celular1.marca}')
print(f'Modelo: {celular1.modelo}')

print('-'*30)
# c. Crie outro objeto da classe "Celular"
celular2 = Celular('Apple', 'iPhone 15 Pro', 'Branco')

# d. Mostre a marca e a cor desse outro celular.
print(f'Marca: {celular2.marca}')
print(f'Cor: {celular2.cor}')