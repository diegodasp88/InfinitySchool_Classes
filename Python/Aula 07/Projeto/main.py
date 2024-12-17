import funcoes as func

# DICIONÁRIO DE CORES ===========================
cor = {
    "vm": "\033[5;31m",
    "vd": "\033[5;32m",
    "am": "\033[5;33m",
    "az": "\033[5;34m",
    "no": "\033[m"
}

# INÍCIO DO PROGRAMA ============================

# MENU ------------------------------------------
while True:
    opcao = func.menu()

    # [1] REGISTRAR VENDA -----------------------
    if opcao == '1':
        func.rg_venda()
    
    # [2] LISTAR PROGRAMA -----------------------
    elif opcao == '2':
        func.listar_cliente()

    # [3] ENCERRAR PROGRAMA -----------------------
    elif opcao == '3':
        func.sortear_clientes()
        break     
        

    # OPÇÃO INVÁLIDA ----------------------------
    else:
        print(f'{cor["vm"]}Opção inválida! Tente novamente.{cor["no"]}')
        time.sleep(2)
        os.system("clear")