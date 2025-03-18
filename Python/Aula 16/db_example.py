import sqlite3

# 1) Criar uma variável que representa a conexão com o db.
conn = sqlite3.connect("./database.db")

# 2) Para executar consultas utilizando a conexão, nós precisamos criar um 'cursor' que será aberto e fechado.
cursor = conn.cursor()

sql = """
    SELECT id, nome, sigla, descricao
    FROM materias
"""

cursor.execute(sql)
dados = cursor.fetchall()

cursor.close() # Fechando o cursor
conn.commit()   # Obrigatório para persistir os dados. Para que de fato os dados sejam adicionados lá no banco de dados.
conn.rollback() # Desfazer o que foi feito para evitar lançamento de erros e retorna à versão anterior antes do erro.

for linha in dados:
    print(linha)