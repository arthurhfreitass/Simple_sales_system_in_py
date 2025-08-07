from db import con, cur

class Produto:
    def __init__(self, nome, descricao, quantidade, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco 


    def salvar_produtos(self):
        comando = """
            INSERT INTO  produtos (nome, descricao, quantidade, preco)
            VALUES(?,?,?,?)
        """

        dados = (self.nome, self.descricao, self.quantidade, self.preco)
        cur.execute(comando, dados)
        con.commit()

def listar_produtos():
    comando = "SELECT * FROM produtos"
    cur.execute(comando)
    produtos = cur.fetchall()
    for produto in produtos:
        id, nome, descricao, quantidade, preco = produto
        print(f"""
Produto ID: {id}
    Nome: {nome}
    Descricao: {descricao}
    Quantidade: {quantidade}
    Preço: {preco}
""")
        
        
def atualizar_quantidade(nova_quantidade, id_produto):

    comando = """UPDATE produtos SET quantidade = ? WHERE ID = ?"""
    cur.execute(comando, (nova_quantidade, id_produto))

    con.commit()


def verificar_produto(id_produto):
    comando = ("SELECT * FROM produtos WHERE ID = ?")
    cur.execute(comando, (id_produto,))
    produto = cur.fetchall()

    return produto


def deletar_produto(id_produto):
    comando = """
    DELETE FROM produtos WHERE id = ?"""
    cur.execute(comando, (id_produto,))

    con.commit()
    con.close()