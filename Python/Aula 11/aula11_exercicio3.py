# Exercício 3: Criem uma Classe "Conta" que deve conter as propriedades:
# - titular
# - saldo (opcional, caso não seja passado começará em 0)

# A classe conta também deve conter os metódos

# - depositar(valor: float)
#     Aumenta o valor do saldo da conta

# - sacar(valor: float)
#     Diminui o valor do saldo da conta, onde não pode
#     ser sacado mais do que há na conta.

# - transferir(valor: float, conta_destino: 'Conta')
#     Irá sacar da conta que chamar esse metódo
#     e depositar na conta que for passada como parametro

class Conta:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        print(f'Seu saldo atual é R${self.saldo}')

    def sacar(self, valor: float):
        if self.saldo > valor:
            self.saldo -= valor
            print(f'Seu saldo atual é R${self.saldo}')
        else:
            raise ValueError('Saldo insuficiente para saque.')

    def transferir(self, valor: float, conta_destino: 'Conta'):
        if self.saldo > valor:
            self.saldo -= valor
            print(f'Seu saldo atual é R${self.saldo}')
            conta_destino.saldo += valor
            print(f'O saldo atual da conta {conta_destino.titular} é R${self.saldo}')
        else:
            raise ValueError('Saldo insuficiente para transferência.')    

conta1 = Conta('Diego DASP')
conta2 = Conta('Diego Perez')

# Depositando valor:
deposito = float(input('Valor a depositar: R$')) 
conta1.depositar(deposito)

# Sacando valor:
saque = float(input('Valor a sacar: R$'))
conta1.sacar(saque)

# Transferindo valor:
transf = float(input('Valor a transferir:'))
conta_destino = Conta()



