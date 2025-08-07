import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()


# cur.execute("CREATE TABLE carrinho(id INTEGER PRIMARY KEY AUTOINCREMENT, id_cliente INTERGE, id_produto INTEGER, nome VARCHAR(250), descricao VARCHAR(500), quantidade INTEGER, preco REAL, FOREIGN KEY (id_produto) REFERENCES produtos (id), FOREIGN KEY (id_cliente) REFERENCES clientes (id))")


# cur.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(250) NOT NULL, email TEXT NOT NULL UNIQUE)")
