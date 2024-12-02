# F U N Ç Ã O:
    # 'def' é a sintaxe usada para definir uma função
def saudacao(nome):
    print(f'Olá {nome}, seja bem-vindo!')

    # Chamando a função (parâmetro definido direto no código)
saudacao('Gabriel')

    # Chamando a função (parâmetro definido pelo usuário)
nome = input('Digite o seu nome: ')
saudacao(nome)


# -------------------------------------------------------

    # Retornando um resultado para a função 
        # 'return' é a sintaxe de saída de resultado da função
def somar(n1, n2):
    return n1 + n2

    # Na chamada da função, após a sua execução, 
    # o retorno assume o lugar da função.
resultado = soma(5, 9)
print(resultado)

    # Printar o retorno diretamente
print(somar(10, 6))

# -------------------------------------------------------

    # Garantindo que não haverá erro no retorno da função
def dividir(n1, n2):
    if n2 == 0:         # divisão por 0 gera erro
        return None     # para não dar erro, retorna None
    
    return n1 / n2

print(dividir(20, 5))
print(dividir(5, 0)) # Daria erro, pois é não é possível dividir por 0.
                     # Só que no caso, agora retorna None.