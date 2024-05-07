CREATE TABLE info_alunos(  
    idAluno int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomeAluno varchar(100),
    turmaAluno char(1)
);
USE defaultdb;
CREATE TABLE info_profs(
    idProf INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nomeProf VARCHAR(150),
    turmaProf CHAR(1) NOT NULL
);
