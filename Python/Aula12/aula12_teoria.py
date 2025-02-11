# -------------------------------------------------------
# Programação Orietada a Objetos (POO) II
# -------------------------------------------------------

# C O E S Ã O:
# Uma classe coesa é uma classe onde a manipulação das propriedades

# E X C E S S Õ E S (EXCEPTIONS):
    # São erros que acontecem em tempo de execução.
    # Esse erro interrompe o fluxo de execução do programa.
    # 'raise' é o comando para chamar uma excessão (erro).

# Estrutura TRY/EXCEPT/FINALLY:
try:
    positivo = float(input('Digite um número positivo: '))

    if positivo <= 0:
        raise ValueError('O valor deve ser positivo')
    
    print(f'{positivo} é um valor válido')

# Caso aconteça um erro esperado, o EXCEPT irá capturar esse erro.
except ValueError as err:
    print(err)

# Finally sempre será executado.
finally:
    print('Fim do programa')
