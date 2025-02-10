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
            raise ValueError('O valor de deposíto deve ser positivo.')

        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        
        if self.saldo < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo.')

        self.saldo -= valor

    def transferir(self, valor: float, conta: 'Conta'):
        self.sacar(valor)
        conta.depositar(valor)

    def __str__(self):
        return f'{self.titular} - {self.saldo_formatado()}'


# Exemplo de Utilização com Input.
# print('Cadastro Banco Infinity.')
# titular = input('Digite o titular da conta: ')

# conta = Conta(titular)

# valor_deposito = float(input('Quanto deseja depositar? '))
# conta.depositar(valor_deposito)
# print(f'Saldo da Conta: {conta.saldo_formatado()}')

# valor_saque = float(input('Quanto deseja sacar? '))
# conta.sacar(valor_saque)
# print(f'Saldo da Conta: {conta.saldo_formatado()}')

c1 = Conta('Diego', 100)
c2 = Conta('Daiana', 30)

print(c1)
print(c2)

c1.transferir(80, c2)

print(c1.saldo_formatado())
print(c2.saldo_formatado())
