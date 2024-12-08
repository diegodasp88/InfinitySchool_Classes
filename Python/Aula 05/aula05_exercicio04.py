'''Ex 04. Faça uma função chamada "cadastrar_pessoa" que não conterá parametros, e irá retornar um dicionário com as chaves "nome", "idade" e "profissao". Os dados serão solicitados através de um input dentro da função.'''

    # Definindo a função cadastrar_pessoa
def cadastrar_pessoa():
    '''Essa função serve para receber os dados do usuários e cadastrar tais dados num dicionário.'''
    cadastro = {}
    cadastro['nome'] = input('Nome: ')
    cadastro['idade'] = int(input('Idade: '))
    cadastro['profissao'] = input('Profissao: ')
    return cadastro

    # Criando uma lista para receber mais cadastros
cadastros = []
novo_cad = 's'  # variável já definida para decisão de um novo cadastro
while novo_cad.lower() == 's':
    dados = cadastrar_pessoa()
    cadastros.append(dados)
    novo_cad = input('Você deseja fazer outro cadastro (s/n)? ')

    # Mostrando os dados para o usuário
for dado in cadastros:
    print(dado)
