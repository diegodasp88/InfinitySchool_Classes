from random import choice

# FUNÇÃO REGISTRAR CLIENTE ======================
def registro_cliente(vendas: list):
    clientes = {}
    clientes["nome"] = input('Nome: ')
    clientes["tel"] = input('Telefone: ')
    clientes["endereco"] = input('Endereço: ')
    vendas.append(clientes)

# FUNÇÃO LISTAR CLIENTES ========================
def listar_cliente(vendas: list):
    for clientes in vendas:
        print(f'Nome: {clientes.get("nome")}')
        print(f'Telefone: {clientes.get("tel")}')
        print(f'Endereço: {clientes.get("endereco")}')
        print('-' * 30)

# FUNÇÃO SORTEAR CLIENTES =======================
def sortear_clientes():
    vencedor = choice(vendas)
    return vencedor


# INÍCIO DO PROGRAMA ============================
vendas = []     # lista de vendas

# MENU ------------------------------------------
while True:
    print()
    print(f' M E N U '.center(30, "="))
    print('[1] Registrar vendas')
    print('[2] Listar vendas')
    print('[3] Encerrar')
    print('-' * 30)
    opcao = input('Digite a opção: ')
    print('-' * 30)

    # [1] REGISTRAR VENDA -----------------------
    if opcao == '1':
        while True:
            print()
            print(' REGISTRAR VENDAS '.center(30, '='))
            registro_cliente(vendas)
            print('-' * 30)
            # fazer novo registro? --------------
            novo = input('Deseja fazer um novo registro (s/n)? ').strip().lower()
            print('-' * 30)
            if novo == 'n':
                break
    
    # [2] LISTAR PROGRAMA -----------------------
    if opcao == '2':
        print()
        print(' LISTAR VENDAS '.center(30, '='))
        listar_cliente(vendas)

    # [3] ENCERRAR PROGRAMA -----------------------
    if opcao == '3':
        print()
        print(' SORTEIO '.center(30, '='))
        vencedor = sortear_clientes()
        print(f'O cliente sorteado é {vencedor}!')
        print('-' * 30)
        print('\nPrograma encerrado...\n')
        break