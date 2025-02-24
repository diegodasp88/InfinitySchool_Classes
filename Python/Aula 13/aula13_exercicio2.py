# Ex02. Aproveitando a classe pessoa criada anteriormente
# Crie uma classe chamada "BancoDePessoas" que será da seguinte forma:

# Atributos:
# - pessoas (list[Pessoa])

# Metódos:
# - adicionar_pessoa(pessoa) | Adiciona uma pessoa na lista
# - buscar_pessoa_pelo_nome(nome) | Busca a pessoa pelo nome, ou retorna "None"
# - remover_pessoa_pelo_nome(nome) | Remove uma pessoa da lista

from datetime import date, datetime

def menu() -> str:
    print(' M E N U '.center(40, '='))
    print('[1] Adicionar pessoas')
    print('[2] Buscar pessoas')
    print('[3] Remover pessoas')
    print('[0] Sair do programa')
    print('-' * 40)
    opcao = input('Digite uma opção: ').strip()
    print('=' * 40)
    return opcao

def menu_buscar() -> str:
    print(' B U S C A R '.center(40, '='))
    print('[1] Mostrar todos cadastradas')
    print('[2] Buscar pessoa pelo nome')
    print('[0] Retornar ao menu principal')
    print('-' * 40)
    opcao = input('Digite uma opção: ').strip()
    print('=' * 40)
    return opcao


class Endereco:
    def __init__(self,
                 cep: str,
                 rua: str,
                 numero: str,
                 bairro: str,
                 cidade: str,
                 estado: str,
                 complemento: str | None = None
                 ):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.complemento = complemento

    def formatar(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
        
    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
        

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, endereco: Endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class BancoDePessoas:
    def __init__(self, pessoas: list[Pessoa]):
        self.pessoas = pessoas

    def adicionar_pessoa(self, pessoa: Pessoa):
        self.pessoas.append(pessoa)

    def buscar_pessoas(self):
        for self.pessoa in self.pessoas:
            print(f'Nome: {self.pessoa.nome}')
            print(f'Data de nascimento: {self.pessoa.data_nascimento}')
            print(f'endereco: {self.pessoa.endereco.formatar()}')


    def buscar_pessoa_pelo_nome(self, nome: str):
        for self.pessoa in self.pessoas:
            if pessoa.nome == nome:
                print(f'Nome: {self.pessoa.nome}')
                print(f'Data de nascimento: {self.pessoa.data_nascimento}')
                print(f'endereco: {self.pessoa.endereco.formatar()}')
            else:
                raise ValueError(f'{nome} não cadastrado.')

    def remover_pessoa_pelo_nome(self, nome: str):
        for self.pessoa in self.pessoas:
            if pessoa.nome == nome:
                print(f'Nome: {self.pessoa.nome}')
                print(f'Data de nascimento: {self.pessoa.data_nascimento}')
                print(f'endereco: {self.pessoa.endereco.formatar()}')
                print('-' * 40)
                conf = input(f'Você deseja deletar {nome}? (s/n): ').strip().lower()
                if conf == 's':
                    self.pessoas.remove(self.pessoa)
                    print(f'{nome} foi removido(a).')
            else:
                raise ValueError('Pessoa não cadastrada.')
            


banco = BancoDePessoas([])

while True:
    opcao = menu()

    # Adicionando pessoas ============================
    if opcao == '1':
        while True:

            # Coletando informações do usuário --------------
            print(' Cadastro de Pessoas '.center(40, '='))
            nome = input('Nome: ').strip().upper()
            data_nascimento = input('Data de Nascimento (dd/MM/yyyy): ').strip()
            data_nasc = datetime.strptime(data_nascimento, '%d/%m/%Y').date() 

            print(' Endereço '.center(40, '-'))
            cep = input('CEP: ').strip()
            rua = input('Logradouro: ').strip().upper()
            numero = input('Número: ').strip()
            bairro = input('Bairro: ').strip().upper()
            cidade = input('Cidade: ').strip().upper()
            estado = input('Estado: ').strip().upper()
            complemento = input('Complemento: ').strip().upper() or None
            print('-' * 40)

            # Criando instâncias -----------------------------
            endereco = Endereco(cep, rua, numero, bairro, cidade, estado, complemento)
            pessoa = Pessoa(nome, data_nascimento, endereco)

            adicionar = input('Você deseja adicionar essa pessoa? (s/n): ').strip().lower()
            if adicionar == 's':
                banco.adicionar_pessoa(pessoa)
                print(f'{pessoa.nome} foi adicionado com sucesso!')
            elif adicionar == 'n':
                print('Cadastro cancelado!')
            else:
                raise ValueError('Digite uma das opções corretas: s / n.')
            print('-' * 40)

            novo = input('Você deseja fazer um novo cadastro? (s/n): ').strip().lower()
            if novo == 's':
                pass
            elif novo == 'n':
                break
            else:
                raise ValueError('Digite uma das opções corretas: s / n.')


    # Buscando pessoas ==============================
    elif opcao == '2':
        while True:
            opcao_buscar = menu_buscar()

            if opcao_buscar == '1':
                banco.buscar_pessoas()
                print('-' * 40)
                cont = input('Pressione ENTER para voltar ao menu.')
            
            elif opcao_buscar == '2':
                while True:
                    nome = input('Digite o nome da pessoa: ').upper()
                    print('-' * 40)
                    banco.buscar_pessoa_pelo_nome(nome)
                    print('-' * 40)
                    
                    novo = input('Você deseja fazer nova busca? (s/n): ').strip().lower()
                    if novo == 's':
                        continue
                    elif novo == 'n':
                        break
                    else:
                        raise ValueError('Digite uma das opções corretas: s / n.')
            
            elif opcao_buscar == '0':
                break

            else:
                raise ValueError('Digite uma das opções corretas.')
    

    if opcao == '3':
        print(' R E M O V E R '.center(40, '='))
        nome = input('Digite o nome da pessoa: ').strip().upper()
        banco.remover_pessoa_pelo_nome(nome)


    if opcao == '0':
        print('Programa finalizado.')
        break
