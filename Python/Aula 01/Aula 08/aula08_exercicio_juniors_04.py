# - Crie uma função chamada media que receba três notas de um aluno e calcule e retorne a média delas.

def media(n1: float, n2: float, n3: float) -> float:
    """Essa função calcula a média entre 3 notas recebidas por um aluno.
    --------------------------
    Parâmetros: 
        n1 (float): nota 1
        n2 (float): nota 2
        n3 (float): nota 3
    -------------------------- 
    Retorna: media (float)"""
    media = (n1 + n2 + n3) / 3
    return media

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

print(f"A média desse aluno é {media(nota1, nota2, nota3):.1f}")