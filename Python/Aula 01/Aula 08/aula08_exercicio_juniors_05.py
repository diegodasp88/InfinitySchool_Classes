# - Crie uma função par_ou_impar que receba um número e retorne uma string informando se o número é "par" ou "ímpar".

def par_ou_impar(num: int) -> str:
    """Essa função reconhece se um número é par ou ímpar.
    ---------------------------
    Parâmetros: num (int)
    ---------------------------
    Retorna: (str)"""
    if num % 2 == 0:
        return "é par!"
    else:
        return "é ímpar!"
    
n = int(input("Insira um número: "))

print(f"Esse número {par_ou_impar(n)}")


