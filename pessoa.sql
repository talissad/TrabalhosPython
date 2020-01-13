SELECT * FROM pessoa
SELECT * FROM endereco

INSERT INTO pessoa(nome, sobrenome, idade)
VALUES('Talissa', 'Dahlke', 22)

INSERT INTO endereco(logradouro, numero, complemento, bairro, cidade, cep)
VALUES('rua 2 de setembro', '2014', 'Ap 1101', 'Centro', 'Blumenau', '89488487')


select 
aulabd.pessoa.Nome, aulabd.endereco.Logradouro
FROM aulabd.pessoa
JOIN aulabd.endereco 
ON aulabd.pessoa.Endereco_id = aulabd.endereco.ID