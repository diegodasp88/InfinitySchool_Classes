# Ex02. Crie uma classe "Imposto" que deve ter um metódo "calcular(valor: float)", que retornará o 0.

class Imposto:
    def calcular(self, valor: float):
        return 0
    
# a. Crie uma classe ISS, que irá herdar de "Imposto", mas o metódo "calcular(valor: float)" deve retornar 6% do valor
class Iss(Imposto):
    def calcular(self, valor: float):
        taxa = 0.06
        return valor * taxa
    
# b. Crie uma outra classe ICMS, que irá herdar de "Imposto", mas o metódo "calcular(valor: float)" deve retornar 4% do valor
class Icms(Imposto):
    def calcular(self, valor: float):
        taxa = 0.04
        return valor * taxa
    

# c. Crie uma função chamada "calcular_impostos" fora das classes, que irá receber o valor, e uma lista com dois objetos das classes "ISS" e "ICMS" respectivamente.
def calcular_imposto(
    valor: float, impostos: list[Imposto]
) -> float:
    total_imposto = 0

    for imposto in impostos:
        total_imposto += imposto.calcular(valor)

    return valor - total_imposto


valor_bruto = float(input('Digite o valor da nota: '))

impostos = [Iss(), Icms()]
valor_liquido = calcular_imposto(valor_bruto, impostos)

print(f'Valor da Nota Bruto: {valor_bruto}')
print(f'Valor da Nota Liquido: {valor_liquido}')
