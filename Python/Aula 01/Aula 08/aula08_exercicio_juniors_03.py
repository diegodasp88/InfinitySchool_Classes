# - Crie uma função calcular_imc que receba o peso e altura de uma pessoa e calcule o Índice de Massa Corporal (IMC), com valores padrões de peso 70 kg e altura 1.75 m.

def calcular_imc(peso: int = 70, altura: float = 1.75) -> float:
    """Essa função calcula o IMC de uma pessoa que possui um peso de 70kg e mede 1,75m de altura.
    -------------------------------
    Parâmetros: 
        peso (int) = 70
        altura (float) = 1.75
    -------------------------------
    Retorna: 
        imc (float)
    """
    imc = peso / altura ** 2
    return imc

print(f"O IMC de uma pessoa que pesa 70kg e possui 1.75m de altura é {calcular_imc():.2f}")