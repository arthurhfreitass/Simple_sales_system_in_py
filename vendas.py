from db import con, cur
from datetime import datetime

class Venda:
    def __init__(self, id_produto, quantidade, preco, data=None, id=None):
        self.id = id
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco = preco
        self.data = data or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def salvar_vendas(self):
        comando =  """
            INSERT INTO vendas (id_produto, quantidade, preco, data)
            VALUES (?, ?, ?, ?)
        """

        dados = (self.id_produto, self.quantidade, self.preco, self.data)

        cur.execute(comando, dados)
        con.commit()