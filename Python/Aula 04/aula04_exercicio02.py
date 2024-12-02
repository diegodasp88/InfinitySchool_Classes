''' Ex 02. Faça uma função "calcular_salario" que recebe um parametro "salario" e retorna o salario deduzido das seguintes taxas:
    - IR: 8%
    - INSS: 5%
    - Sindicato: 3%'''

# Definição da função
def calcular_salario(salario):
    desc_ir =  0.08
    desc_inss = 0.05
    desc_sind = 0.03
    sal_liq = salario * (1 - desc_ir - desc_inss - desc_sind)
    return sal_liq

# ENTRADA: coletando dados do usuário
sal = float(input('Digite o salário bruto: R$ '))

# SAÍDA: mostrando a resposta
print(f'O salário líquido é R$ {calcular_salario(sal):.2f}')
