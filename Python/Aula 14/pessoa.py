from dataclasses import dataclass
from datetime import date
from endereco import Endereco
from tabulate import tabulate

@dataclass
class Pessoa:     
    nome: str
    cpf: str
    data_nascimento: date
    endereco: Endereco


class PessoaRepository:
    dados: list[Pessoa] = []

    def adicionar(self, pessoa: Pessoa):
        self.dados.append(pessoa)

    def buscar_todos(self, pessoa: Pessoa):
        for pessoa in self.dados:
            print(f'Nome: {pessoa.nome}')
            print(f'CPF: {pessoa.cpf}')
            print(f'Data de nascimento: {pessoa.data_nascimento}')

    def buscar_pelo_cpf(self, cpf: str):
        for pessoa in self.dados:
            if pessoa.cpf == cpf:
                return pessoa
        return None
    