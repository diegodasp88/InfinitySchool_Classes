# Ex01. Crie uma classe "Pessoa" que deve conter:

# Atributos
# - nome (str)
# - data_nascimento (date)
# - endereco (Endereco)

# A propriedade "endereco" será uma outra classe "Endereco" que terá:

# Atributos
# - cep (str)
# - rua (str)
# - numero (str)
# - bairro (str)
# - cidade (str)
# - estado (str)
# - complemento (str)

# Metódos:
# - formatar() | Retorna o endereço formatado em uma String

# A formatação será:
# "Rua, Numero - Bairro | Cidade - Estado, Cep"
# ==========================================================

from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class Endereco:
    cep: str
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    complemento: str | None = None

    def formatar(self) -> str:
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    
    # Diz como o objeto será formatado para o USUÁRIO.
    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    
    # Diz como o objeto será formatado para o DESENVOLVEDOR.
    def __repr__(self):
        return Endereco(cep="{self.cep}", 
                        rua="{self.rua}", 
                        numero="{self.numero}",
                        bairro="{self.bairro}",
                        cidade="{self.cidade}",
                        estado="{self.estado}",
                        complemento="{self.complemento"
                        )

@dataclass
class Pessoa:
    nome: str
    data_nascimento: date
    endereco: Endereco


print(' Cadastro de Usuário '.center(40, '='))
nome = input('Nome: ')
data_nascimento = input('Data de Nascimento (dd/MM/yyyy): ')
data_nasc = datetime.strptime(data_nascimento, '%d/%m/%Y').date() 

print(' Endereço '.center(40, '-'))
cep = input('CEP: ')
rua = input('Logradouro: ')
numero = input('Número: ')
bairro = input('Bairro: ')
cidade = input('Cidade: ')
estado = input('Estado: ')
complemento = input('Complemento: ')
print(' Cadastro de Usuário '.center(40, '='))

endereco = Endereco(cep, rua, numero, bairro, cidade, estado, complemento)
usuario = Pessoa(nome, data_nascimento, endereco)

print(usuario.nome)
print(usuario.data_nascimento)
print(usuario.endereco.formatar())
