# Ex02. Crie uma classe "Imposto" que deve ter um metódo "calcular(valor: float)", que retornará o proprio valor.

class Imposto:
    def calcular(self, valor: float):
        return valor

# a. Crie uma classe ISS, que irá herdar de "Imposto", mas o metódo "calcular(valor: float)" deve retornar o valor do imposto com uma dedução de 6%
class ISS(Imposto):
    def calcular(self, valor: float):
        imposto = 0.06
        return valor * (1 - imposto)

# b. Crie uma outra classe ICMS, que irá herdar de "Imposto", mas o método "calcular(valor: float)" deve retornar o valor do imposto com uma dedução de 7%
class ICMS(Imposto):
    def calcular(self, valor: float):
        imposto = 0.07
        return valor * (1 - imposto)

# c. Crie uma função chamada "calcular_impostos" fora das classes, que irá receber o valor, e uma lista com dois objetos das classes "ISS" e "ICMS" respectivamente.
def calcular_impostos(valor: float, impostos: list = [ISS, ICMS]):
    for imposto in impostos:
        print(f'{imposto.__class__.__name__}: R${imposto.calcular(valor):.2f}')

# Criando instâncias das classes
iss = ISS()
icms = ICMS()
valor = float(input('Digite o valor: R$'))

# Chamando a função com os impostos
calcular_impostos(valor, [iss, icms])