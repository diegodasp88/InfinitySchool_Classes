''' Ex 04. Você foi contratado por uma instituição de nutrição para ajuda-los em um sistema:

a. Faça uma função chamada "calcular_imc" que irá receber dois parametros ("peso" e "altura") e retornar o valor do IMC.
b. Faça uma função chamada "classificar_imc" que recebe o IMC e retorna uma string com a situação da pessoa baseado na tabela IMC:

- "ABAIXO_DO_PESO"  -> Imc <= 18.5
- "PESO_IDEAL"      -> Imc <= 25
- "SOBREPESO"       -> Imc <= 30
- "OBESIDADE_I"     -> imc <= 35
- "OBESIDADE_II"    -> imc <= 40
- "OBESIDADE_III"   -> imc > 40 '''

    # Definindo a função (a)
def calcular_imc(peso, altura):
    cal_imc = peso / altura ** 2
    return cal_imc

    # Definindo a função (b)
def classificar_imc(imc):
    if imc <= 18.5:
        return 'Abaixo do peso.'
    elif imc <= 25:
        return 'Peso ideal.'
    elif imc <= 30:
        return 'Sobrepeso'
    elif imc <= 35:
        return 'Obesidade I'
    elif imc <= 40:
        return 'Obesidade II'
    else:
        return 'Obesidade III'

    # ENTRADA: coletando dados do usuário     
weight = float(input('Digite o peso: (kg) '))
height = float(input('Digite a altura: (m) '))

    # PROCESSAMENTO: calculando o IMC (chamando a função)
imc = calcular_imc(weight, height)

    #SAÍDA: mostrar o resultado
print(f'Seu IMC é {imc:.1f} e você se encontra na classificação de {classificar_imc(imc)}')