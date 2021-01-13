-- CRIANDO A TABELA
create table usuarios(
    nome VARCHAR(50),
    email VARCHAR(100),
    idade INT
);

-- INSERINDO DADOS

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Eduardo Portella", 
    "eportella70@gmail.com", 
    19
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "João Silva",
    "joaosilva@email.com",
    51
);

INSERT INTO usuarios(idade, nome, email) VALUES(
    30,
    "Maria Santos",
    "mariasantos@email.com"
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Nome legal",
    "nomelegal@email.com",
    55
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Ana Portella",
    "anaportella@gmail.com",
    15
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Gilmar Portella",
    "gilmarportella@gmail.com",
    58
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Valdirene Portella",
    "valdireneportella@gmail.com",
    47
);

INSERT INTO usuarios(nome, email, idade) VALUES(
    "Maria Silva",
    "mariasilva@gmail.com",
    19
);

-- BUSCANDO DADOS

SELECT * FROM usuarios WHERE idade = 19;

SELECT * FROM usuarios WHERE nome = "Eduardo Portella";

SELECT * FROM usuarios WHERE idade >= 18;

--DELETANDO DADOS

DELETE FROM usuarios WHERE nome = "Nome Legal";

--ATUALIZANDO DADOS

UPDATE usuarios SET nome = "Nome de Teste", email = "emaildeteste@email.com" WHERE nome = "Maria Silva" && idade = 19;