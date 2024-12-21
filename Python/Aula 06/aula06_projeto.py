from random import choice
from time import sleep
from os import system

# DICIONÁRIO DE CORES ===========================
cor = {
    "vm": "\033[5;31m",
    "vd": "\033[5;32m",
    "am": "\033[5;33m",
    "az": "\033[5;34m",
    "no": "\033[m"
}

# FUNÇÃO REGISTRAR CLIENTE ======================
def registro_cliente(vendas: list):
    clientes = {}
    clientes["nome"] = input(f'{cor["az"]}Nome: {cor["no"]}').strip()
    clientes["tel"] = input(f'{cor["az"]}Telefone: {cor["no"]}').strip()
    clientes["endereco"] = input(f'{cor["az"]}Endereço: {cor["no"]}').strip()
    vendas.append(clientes)

# FUNÇÃO LISTAR CLIENTES ========================
def listar_cliente(vendas: list):
    for clientes in vendas:
        print(f'{cor["az"]}Nome:{cor["no"]} {clientes.get("nome")}')
        print(f'{cor["az"]}Telefone:{cor["no"]} {clientes.get("tel")}')
        print(f'{cor["az"]}Endereço:{cor["no"]} {clientes.get("endereco")}')
        print('-' * 40)

# FUNÇÃO SORTEAR CLIENTES =======================
def sortear_clientes():
    vencedor = choice(vendas)
    return vencedor


# INÍCIO DO PROGRAMA ============================
vendas = []     # lista de vendas

# MENU ------------------------------------------
while True:
    print()
    print(f' M E N U '.center(40, "="))
    print(f'{cor["am"]}[1]{cor["az"]} Registrar vendas{cor["no"]}')
    print(f'{cor["am"]}[2]{cor["az"]} Listar vendas{cor["no"]}')
    print(f'{cor["am"]}[3]{cor["az"]} Encerrar{cor["no"]}')
    print('-' * 40)
    opcao = input(f'{cor["am"]}Digite a opção: {cor["no"]}')
    print('-' * 40)

    # [1] REGISTRAR VENDA -----------------------
    if opcao == '1':
        while True:
            print()
            print(' REGISTRAR VENDAS '.center(40, '='))
            registro_cliente(vendas)
            # mensagem de venda bem sucedida ----
            print(f'{cor["vd"]}Venda realizada com sucesso!{cor["no"]}')
            print('-' * 40)
            sleep(1)
            # fazer novo registro? --------------
            novo = input(f'{cor["am"]}Deseja fazer uma nova venda (s/n)? {cor["no"]}').strip().lower()
            print('-' * 40)
            if novo == 'n':
                sleep(2)
                system("clear")
                break
    
    # [2] LISTAR PROGRAMA -----------------------
    elif opcao == '2':
        print()
        print(' LISTAR VENDAS '.center(40, '='))
        listar_cliente(vendas)
        cont = input(f'{cor["am"]}Enter para continuar...{cor["no"]}')
        sleep(1)
        system("clear")

    # [3] ENCERRAR PROGRAMA -----------------------
    elif opcao == '3':
        print()
        print(' SORTEIO '.center(40, '='))
        vencedor = sortear_clientes()
        print(f'{cor["am"]}O cliente sorteado é...{cor["no"]}')
        sleep(2)
        print(f'Nome: {cor["vd"]}{vencedor["nome"]}{cor["no"]}\nTelefone: {cor["vd"]}{vencedor["tel"]}{cor["no"]} \nEndereço: {cor["vd"]}{vencedor["endereco"]}{cor["no"]}')
        print('-' * 40)
        print(f'\n{cor["am"]}Programa encerrado...{cor["no"]}\n')
        break

    # OPÇÃO INVÁLIDA ----------------------------
    else:
        print(f'{cor["vm"]}Opção inválida! Tente novamente.{cor["no"]}')
        sleep(2)
        system("clear")
