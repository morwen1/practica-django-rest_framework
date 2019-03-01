
DROP TABLE if exists usuarios ;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nikname varchar(25),
    pasword varchar(255),
    patos integer REFERENCES patos(id) ON DELETE CASCADE
);

DROP TABLE if exists patos;

CREATE TABLE  patos ( 
    id  SERIAL PRIMARY KEY ,
    nombre  varchar(200),
    segundo_nombre varchar(200),
    edad  int
    
    
);

INSERT into usuarios(nikname,patos,pasword) 
values ("perro",1,"dasd");