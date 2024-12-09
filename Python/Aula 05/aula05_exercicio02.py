'''Ex 02. Faça uma função chamada "verificar_par" que recebe um número inteiro e retorna um booleano (True se for par, False se for impar)'''

    # Definindo a função
def verificar_par(num: int) -> bool:
    """Função que verifica se o número é par ou não
        Arg: num (int)
        Returns: (bool)
    """
    if num % 2 == 0:
        return True
    else:
        return False

    # ENTRADA: coletando dados do usuário
num = int(input('Digite um número: '))

    # PROCESSAMENTO: chamando a função para definir se é par ou não
eh_par = verificar_par(num)
if eh_par == True:
    eh_par = 'Verdade'
else:
    eh_par = 'Falso'

    # SAÍDA: mostrando o resultado
print(f'É {eh_par.lower()} que o número {num} seja par.')
