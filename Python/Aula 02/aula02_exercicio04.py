# Ex 04. Dado o dicionário abaixo, que representa o salário de diferentes cargos em uma empresa, 
# some os salários de todos os cargos e exiba o total.

"""python
salarios = {
    "gerente": 5000, 
    "analista": 4000, 
    "desenvolvedor": 3500, 
    "estagiário": 1500
}
"""
salarios = {
    "gerente": 5000, 
    "analista": 4000, 
    "desenvolvedor": 3500, 
    "estagiário": 1500
}
soma = sum(salarios.values())
print(f'A soma dos salários da empresa é R${soma:.2f}.')