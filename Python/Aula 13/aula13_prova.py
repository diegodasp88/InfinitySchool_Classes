class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError('O saldo deve ser zerado ou positivo.')
        self.__titular = titular
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo: float):
        if novo_saldo:
            self.__saldo = novo_saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: float):
        if novo_titular:
            self.__titular = novo_titular

    # Operações bancárias
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser positivo.')
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        if self.saldo < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo.')
        self.saldo -= valor

    def exibir_saldo(self, valor: float):
        print(f'Saldo Atual: R${valor:.2f}')


# Definindo o titular e o saldo
conta = ContaBancaria('Diego', 10000)
print("CONTA BANCÁRIA".center(30, '-'))
print(f'Titular: {conta.titular}')
conta.exibir_saldo(conta.saldo)
print('-' * 30)

# Depositando
print("DEPÓSITO".center(30, '-'))
valor_dep = 5000
print(f'Valor depositado: {valor_dep:.2f}')
conta.depositar(valor_dep)
conta.exibir_saldo(conta.saldo)
print('-' * 30)

# Sacando
print("SAQUE".center(30, '-'))
valor_saq = 3000
print(f'Valor sacado: {valor_saq:.2f}')
conta.sacar(valor_saq)
conta.exibir_saldo(conta.saldo)
print('-' * 30)