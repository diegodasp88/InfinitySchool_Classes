# H E R A N Ç A:
# Capacidade de uma classe de herdar os mesmos atributos de uma classe mãe.

# P O L I M O R F I S M O:
# Capacidade de sobrescrever um método herdado da classe mãe para o próprio método.


class ContaMae:
    # Metódo Construtor
    def __init__(self, titular: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError('O saldo deve ser zerado ou positivo.')
        self.titular = titular
        self.saldo = saldo
    
    def saldo_formatado(self) -> str:
        valor = str(round(self.saldo, 2)).replace('.', ',')
        return f'R$ {valor}'

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

    def transferir(self, valor: float, conta: 'ContaMae'):
        self.sacar(valor)
        conta.depositar(valor)

    def __str__(self):
        return f'{self.titular} - {self.saldo_formatado()}'
    

    
class ContaCorrente(ContaMae): # Herança: herdando os métodos da classe ContaMae
    # Polimorfismo
    def __init__(self, titular: str, saldo: float = 0, chq_especial: float = 0):
        super().__init__(titular, saldo)
        self.chq_especial = chq_especial
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        if self.saldo + self.chq_especial < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo + cheque especial.')
        
    
class ContaPoupanca(ContaMae): # Herança: herdando os métodos da classe ContaMae
    pass

conta_corrente = ContaCorrente('Diego', 100, 50)

print(conta_corrente)
conta_corrente.sacar(160)
print(conta_corrente)