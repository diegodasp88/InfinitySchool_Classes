from db import conn
import os


def listar_materias():
    cursor = conn.cursor()
    sql = """
    SELECT id, nome, sigla, descricao
    FROM materias
    """
    cursor.execute(sql)
    dados = cursor.fetchall()
    cursor.close()
    return dados

def buscar_materia_por_sigla():
    cursor = conn.cursor()
    sql = """
    SELECT id, nome, sigla, descricao
    FROM materias
    WHERE sigla = ?
    """
    cursor.execute(sql, (nome, ))
    dados = cursor.fetchall()
    cursor.close()
    return dados


def cadastrar_materia(nome: str, sigla: str, descricao: str | None = None):
    cursor = conn.cursor()
    sql = """
    INSERT INTO materias (nome, sigla, descricao)
    VALUES (?, ?, ?)
    """
    cursor.execute(sql, (nome, sigla, descricao))   # Os parâmetros para serem preenchidos são informados dentre parênteses.
    dados = cursor.fetchall()
    cursor.close()
    conn.commit()   # Obrigatório para persistir os dados. Para que de fato os dados sejam adicionados lá no banco de dados.


def menu():
    while True:
        os.system("clear")
        print(" M E N U ".center(40, "-"))
        print("[1] Listar matérias")
        print("[2] Cadastrar matérias")
        print("[3] Voltar")
        print("-"*40)
        opcao = input("Digite a opção: ").strip()
        print("-"*40)

        if opcao == "1":
            materias = listar_materias()
            for id, nome, sigla, _ in materias:
                print(f"{id} - {nome} ({sigla})")

        elif opcao == "2":
            materia = input("Nome da matéria: ").strip()
            sigla = input("Sigla da matéria: ").strip()
            descricao = input("Descrição: ").strip()
            if descricao == "":
                descricao = None

        elif opcao == "3":
            break


if __name__ == "__main__":
    menu()