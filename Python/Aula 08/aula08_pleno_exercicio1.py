# - Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (como uma string: "soma", "subtração", "multiplicação", "divisão"). A função deve retornar o resultado da operação escolhida entre os dois números.

def calculadora(n1: int, n2: int, op: str) -> float:
    '''Essa função recebe 2 números inteiros e permite ao usuário escolher qual operação ele gostaria de fazer para receber o seu resultado.
    =========================
    Parâmetros:
        n1 (int): 1º número inteiro
        n2 (int): 2º número inteiro
        op (str): operação = ("+","-","*","/")
    -------------------------
    Retorna:
        resultado (float)'''
    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    elif op == "/":
        resultado = n1 / n2
    else:
        resultado = "Sinal de operação não válido, favor escolher entre (+, -, * ou /)."
    return resultado
    
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
sinal = input('Escolha a operação desejada (+, -, *, /): ')

resultado = calculadora(num1, num2, sinal)
print(f'{num1} {sinal} {num2} = {resultado}')
