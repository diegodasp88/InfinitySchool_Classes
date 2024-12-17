import random as rd
import time
import os
import funcoes as func

# DICIONÁRIO DE CORES ===========================
cor = {
    "vm": "\033[5;31m",
    "vd": "\033[5;32m",
    "am": "\033[5;33m",
    "az": "\033[5;34m",
    "no": "\033[m"
}

# LISTA DE VENDAS ===============================
vendas = []     # lista de vendas

# FUNÇÃO MENU PRINCIPAL =========================
def menu():
    print()
    print(f' M E N U '.center(40, "="))
    print(f'{cor["am"]}[1]{cor["az"]} Registrar vendas{cor["no"]}')
    print(f'{cor["am"]}[2]{cor["az"]} Listar vendas{cor["no"]}')
    print(f'{cor["am"]}[3]{cor["az"]} Encerrar{cor["no"]}')
    print('-' * 40)
    opcao = input(f'{cor["am"]}Digite a opção: {cor["no"]}')
    print('-' * 40)
    return opcao

# FUNÇÃO REGISTRAR CLIENTE ======================
def rg_venda():
    clientes = {}
    while True:
        print()
        print(' REGISTRAR VENDAS '.center(40, '='))
        clientes["nome"] = input(f'{cor["az"]}Nome: {cor["no"]}').strip()
        clientes["tel"] = input(f'{cor["az"]}Telefone: {cor["no"]}').strip()
        clientes["endereco"] = input(f'{cor["az"]}Endereço: {cor["no"]}').strip()
        vendas.append(clientes)
        # mensagem de venda bem sucedida ----
        print(f'{cor["vd"]}Venda realizada com sucesso!{cor["no"]}')
        print('-' * 40)
        time.sleep(1)
        # fazer novo registro? --------------
        novo = input(f'{cor["am"]}Deseja fazer uma nova venda (s/n)? {cor["no"]}').strip().lower()
        print('-' * 40)
        if novo == 'n':
            time.sleep(2)
            os.system("clear")
            break


# FUNÇÃO LISTAR CLIENTES ========================
def listar_cliente():
    for clientes in vendas:
        print()
        print(' LISTAR VENDAS '.center(40, '='))
        print(f'{cor["az"]}Nome:{cor["no"]} {clientes.get("nome")}')
        print(f'{cor["az"]}Telefone:{cor["no"]} {clientes.get("tel")}')
        print(f'{cor["az"]}Endereço:{cor["no"]} {clientes.get("endereco")}')
        print('-' * 40)
        cont = input(f'{cor["am"]}Enter para continuar...{cor["no"]}')
        time.sleep(1)
        os.system("clear")

# FUNÇÃO SORTEAR CLIENTES =======================
def sortear_clientes():
    print()
    print(' SORTEIO '.center(40, '='))
    vencedor = rd.choice(vendas)
    print(f'{cor["am"]}O cliente sorteado é...{cor["no"]}')
    time.sleep(2)
    print(f'Nome: {cor["vd"]}{vencedor["nome"]}{cor["no"]}\nTelefone: {cor["vd"]}{vencedor["tel"]}{cor["no"]} \nEndereço: {cor["vd"]}{vencedor["endereco"]}{cor["no"]}')
    print('-' * 40)
    print(f'\n{cor["am"]}Programa encerrado...{cor["no"]}\n')