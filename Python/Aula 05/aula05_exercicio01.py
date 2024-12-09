'''Ex 01. Faça uma função "calcular_media" que recebe 3 numeros e retorna a média desses numeros.'''

    # Definindo a função
def calcular_media(num1: float, num2: float, num3: float) -> float:
    """Função feita para retornar a média aritmética entre 3 números flutuantes."""
    media = (num1 + num2 + num3) / 3
    return media

    # ENTRADA: coletando dados do usuário
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

    # PROCESSAMENTO: Chamando a função para calcular a média
avg = calcular_media(n1, n2, n3)

    # SAÍDA: mostrando o resultado
print(f'A média dos números informados é {avg:.1f}')
