-- Active: 1715092745082@@pi-2024-omateocortez.c.aivencloud.com@22705@PyMemoryDB



-- Criar banco de dados
CREATE DATABASE PyMemoryDB;
-- Usar banco de dados
USE PyMemoryDB;


-- criar tabela de alunos
CREATE TABLE turmas(
    idTurma INT NOT NULL AUTO_INCREMENT,
    turma CHAR(1) NOT NULL PRIMARY KEY,
UNIQUE KEY(idTurma)
);


-- criar tabela de alunos
CREATE TABLE tb_alunos(
    idAluno INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomeAluno VARCHAR(255) NOT NULL,
    turmaAluno CHAR(1),
        FOREIGN KEY (turmaAluno) REFERENCES turmas(turma)
);

-- criar tabela de funcionários
CREATE TABLE tb_funcionarios(
    idFunc INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nomeFunc VARCHAR(255) NOT NULL,
    turmaFunc CHAR(1),
    funcao VARCHAR(255) DEFAULT 'Professor',
        FOREIGN KEY (turmaFunc) REFERENCES turmas(turma)
);