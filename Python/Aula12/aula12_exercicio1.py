# Ex01. Crie uma classe chamada "Funcionario" que deve ter os atributos e metódos:

# Atributos:
# - nome
# - salario

# Metódos:
# - calcular_salario()

# O calcular salário deve retornar o salario com uma dedução de 3%.

# a. Crie uma classe "Gerente" que deve ter os mesmos atributos do Funcionário, mas a dedução do salário deve ser de 11% no "calcular_salario()".

# b. Crie uma classe "Vendedor" que deve ter um atributo de "comissao: float", que será informado no construtor. O salario deve ter uma dedução de 8% "calcular_salario()" mas deve somar o valor da comissão.

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario(self) -> float:
        imposto = 0.03
        return self.salario * (1 - imposto)
    
    def info(self):
        print('='*30)
        print(f'Funcionário: {self.nome}')
        print(f'Salário Bruto: R${self.salario:.2f}')
        print(f'Salário Líquido: R${self.calcular_salario():.2f}')
    
class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_salario(self) -> float:
        imposto = 0.11
        return self.salario * (1 - imposto)
    
    def info(self):
        return super().info()
    
class Vendedor(Funcionario):
    def __init__(self, nome: str, salario: float, comissao: float):
        super().__init__(nome, salario)
        self.comissao = comissao
    
    def calcular_salario(self) -> float:
        imposto = 0.08
        return self.salario * (1 - imposto) + comissao
    
    def info(self):
        print('='*30)
        print(f'Funcionário: {self.nome}')
        print(f'Salário Bruto: R${self.salario:.2f}')
        print(f'Comissão: R${self.comissao:.2f}')
        print(f'Salário Líquido: R${self.calcular_salario():.2f}')


print(' Cálculo de salário '.center(30, '='))
print('[1] - Funcionário')
print('[2] - Gerente')
print('[3] - Vendedor')
print('-'*30)
opcao = int(input('Digite a opção desejada: '))
print('-'*30)

nome = input('Insira o nome do empregado: ')
salario = float(input('Insira o salário do empregado: R$'))

if opcao == 1:
    empregado = Funcionario(nome, salario)
    empregado.info()
elif opcao == 2:
    empregado = Gerente(nome, salario)
    empregado.info()
elif opcao == 3:
    comissao = float(input('Insira a comissão do empregado: R$'))
    empregado = Vendedor(nome, salario, comissao)
    empregado.info()
