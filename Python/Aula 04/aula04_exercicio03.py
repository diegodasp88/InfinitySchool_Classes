''' Ex 03. Faça uma função chamada "calcular_area_retangulo" que recebe dois parametros ("base" e "altura") e retorna a area do retangulo.'''

    # Definindo a função
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

    # ENTRADA: coletando dados do usuário
b = float(input('Digite o valor da base do retângulo: '))
h = float(input('Digite o valor da altura do retângulo: '))

    # SAÍDA: mostrando o resultado, já utilizando a função
print(f'A área do retângulo equivale a {calcular_area_retangulo(b, h):.1f}')
