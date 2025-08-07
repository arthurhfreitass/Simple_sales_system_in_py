from db import cur, con
import re

class Clientes:
    def __init__(self,  id_cliente, nome, email):
        self.id = id_cliente
        self.nome = nome
        self.email = email

    def salvar_clientes(self):
        comando = ("""INSERT INTO clientes ( nome, email) 
                      VALUES (?,?,?,?)
                    """)
        
        dados = (self.id_cliente, self.nome, self.email)

        cur.execute(comando, dados)
        con.commit()


def verificar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None


def cadastro(nome, email):
    comando = ("""INSERT INTO clientes (nome, email) VALUES (?, ?)""")

    dados = (nome, email)

    cur.execute(comando, dados)
    con.commit()


def verificar_cadastro(email):
    comando = ("""SELECT * FROM clientes WHERE email = ?""")
    cur.execute(comando, (email,))
    cliente = cur.fetchone

    return cliente is not None



def verificar_login(email):
    comando = ("""SELECT id FROM clientes WHERE email = ?""")
    cur.execute(comando, (email,))
    cliente = cur.fetchone()

    if cliente:
        id_cliente = cliente

        return id_cliente[0]
    else:
        return None

        

    
        