from endereco import Endereco
from pessoa import Pessoa, PessoaRepository
from menu import main_menu, listar_menu

from datetime import date, datetime
from os import system


pessoa_repository = PessoaRepository()

while True:
    opcao = main_menu()

    # CADASTRO ==================================
    if opcao == '1':
        while True:
            system('clear')
            print(' Cadastro de Pessoas '.center(40, '='))
            nome = input('Nome: ').strip().upper()

            # Validação CPF no cadastro *********
            cpf = input('CPF: ').strip()
            validar_cpf = pessoa_repository.buscar_pelo_cpf(cpf)
            if validar_cpf != None:
                print('CPF já cadastrado no sistema.')
                input('Pressione ENTER para continuar...')
                continue

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

            # Criando instâncias ****************
            endereco = Endereco(cep, rua, numero, bairro, cidade, estado, complemento)
            pessoa = Pessoa(nome, cpf, data_nascimento, endereco)

            # Confirmar cadastro ****************
            while True:
                try:
                    adicionar = input('Cadastrar pessoa? (S/N): ').strip().upper()
                    if adicionar == 'S':
                        pessoa_repository.adicionar(pessoa)
                        print(f'{pessoa.nome} foi cadastrado com sucesso!')
                        print('-' * 40)
                        break
                    elif adicionar == 'N':
                        print('Cadastro cancelado!')
                        print('-' * 40)
                        break
                    else: 
                        raise ValueError('Opção inválida. Digite "S" ou "N".')          
                except ValueError as erro:
                    print(erro)
                    print('-' * 40)

            # Fazer novo cadastro? ------------------
            while True:    
                try:
                    novo = input('Fazer um novo cadastro? (S/N): ').strip().upper()
                    if novo == 'S':
                        break
                    elif novo == 'N':
                        break
                    else: 
                        raise ValueError('Opção inválida. Digite "S" ou "N".')          
                except ValueError as erro:
                    print(erro)
                    print('-' * 40)

            # Não fazer novo cadastro
            if novo == 'N':
                break    


    # LISTAR ====================================
    elif opcao == '2':
        while True:
            opcao_listar = listar_menu()

            # Listar todos as pessoas ***************
            if opcao_listar == '1':
                if len(pessoa_repository)
                pessoa_repository.buscar_todos()

            elif opcao_listar == '0':
                break


    # SAIR ======================================
    elif opcao == '0':
        print('Programa encerrado.')
        break