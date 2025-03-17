-- DDL (Data Definition Language)

-- MySQL/PostgreSQL: 
-- CREATE DATABASE <meu_banco>; --> (criar banco de dados)
-- USE <meu_banco>; --> (usar banco de dados)

-----------------------------------------------------------
-- Criando Tabela
CREATE TABLE alunos (
-- <coluna> <tipo> <característica>
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(255) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	observacao VARCHAR(255),
	ativo INT NOT NULL DEFAULT 1
);

-----------------------------------------------------------
-- Excluindo Tabela
DROP TABLE alunos;

-----------------------------------------------------------
-- DQL (Data Query Language)

SELECT * FROM alunos;

SELECT id, nome, registro FROM professores;

-----------------------------------------------------------
-- DML (Data Manipulation Language)

-- Inserir valores em uma tabela
INSERT INTO alunos (nome, cpf, data_nascimento)
VALUES ('Diego', '12345678900', '1988-11-02'),
       ('Tulio', '11122233344', '1998-03-11');

-- Deletar valores de uma tabela
DELETE FROM alunos 
WHERE id = 2;
/*
Se você executar o DELETE sem a cláusula WHERE, 
você exclui todas as linhas da tabela.
 */


-- Atualizar os valores de uma tabela
UPDATE alunos
SET nome = 'Diego DASP'
WHERE id = 1;
/*
Se você executar o UPDATE sem a cláusula WHERE, 
você atualiza todas as linhas da tabela onde as colunas 
forem especificadas no comando SET.
*/
-----------------------------------------------------------

-----------------------------------------------------------

 /*
Ex01. Crie uma tabela chamada "professores" que deve conter as seguintes colunas

- nome (String)
- registro (String, 5 Caracteres e deve ser UNICO)
- data_nascimento (Date)
- sobre (String, opcional)

OBS: A coluna ID é implicita.
*/

CREATE TABLE professores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(255) NOT NULL,
	registro VARCHAR(5) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	sobre VARCHAR(255)
);

---------------------------------------------------------
