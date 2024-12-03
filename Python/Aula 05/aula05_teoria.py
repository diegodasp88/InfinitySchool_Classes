# T Y P E   H I N T
    # Especifica os tipos esperados nos parâmetros e nos retornos de funções. Exemplo:

def multiplicar(n1:float, n2:float) -> float:
    return n1 * n2

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print(multiplicar(num1, num2))


# ----------------------------------------------------------------

# D O C S T R I N G
    # Cria um texto (str) explicativo para ajudar ao programador a utilizar a função sem dificuldades. Exemplo:

def dividir(n3:float, n4:float) -> float:
    '''
    Essa função retorna a divisão de dois números

    Parâmetros:
        - n3 (float)
        - n4 (float)

    Retorna: (float)
    '''
    return n3 / n4

num3 = float(input('Digite um número: '))
num4 = float(input('Digite outro número: '))

print(dividir(num3, num4))