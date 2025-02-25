from os import system

def main_menu() -> str:
    system('clear')
    print(' M E N U '.center(40, '='))
    print('[1] Cadastrar')
    print('[2] Listar')
    print('[3] Remover')
    print('[4] Editar')
    print('[0] Sair')
    print('-' * 40)
    opcao = input('Digite uma opção: ').strip()
    print('=' * 40)
    return opcao


def listar_menu() -> str:
    system('clear')
    print(' L I S T A R '.center(40, '='))
    print('[1] Listar cadastro')
    print('[2] Listar por CPF')
    print('[0] Retornar ao menu principal')
    print('-' * 40)
    opcao = input('Digite uma opção: ').strip()
    print('=' * 40)
    return opcao


