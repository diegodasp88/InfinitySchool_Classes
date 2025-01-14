# - Crie uma função chamada contagem_regressiva que recebe um número n e imprime os números de n até 1, em contagem regressiva.
import time

def contagem_regressiva(n: int):
    """Essa função faz uma contagem regressiva desde o número inserido pelo usuário até 1.
    ----------------------
    Parâmetros: 
        n (int)"""
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)


num = int(input("Digite o número incial da contagem regressiva: "))
contagem_regressiva(num)