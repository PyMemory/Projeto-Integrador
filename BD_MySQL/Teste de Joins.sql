-- Active: 1715092745082@@pi-2024-omateocortez.c.aivencloud.com@22705@PyMemoryDB

SELECT *
FROM tb_alunos AS a
JOIN tb_funcionarios AS f ON a.turmaAluno = f.turmaFunc


SELECT a.nomeAluno, f.nomeFunc, a.turmaAluno
FROM tb_alunos AS a
JOIN tb_funcionarios AS f ON a.turmaAluno = f.turmaFunc
