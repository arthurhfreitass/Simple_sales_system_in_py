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
        comando = """
            INSERT INTO vendas (id_produto, quantidade, preco, data)
            VALUES (?, ?, ?, ?)
        """

        dados = (self.id_produto, self.quantidade, self.preco, self.data)

        cur.execute(comando, dados)
        con.commit()


def selecionar_produto(id_produto, id_cliente):
    comando = "SELECT * FROM produtos WHERE ID = ?"
    cur.execute(comando, (id_produto,))
    produto_escolhido = cur.fetchall()

    for produto in produto_escolhido:
        if produto:
            id, nome, descricao, quantidade, preco = produto
            print("-----" * 4)
            print("  Item escolhido")
            print("-----" * 4)
            print(f"  Id do produto: {id}")
            print(f"  {nome}")
            print(f"  {descricao}")
            print(f"  Quantidade disponivel: {quantidade}")
            print(f"  Valor: {preco}")

            print()
            quantidade_produto = int(input("Selecione a quantidade desejada: "))

            if quantidade_produto <= quantidade:
                calculando_preco = preco * quantidade_produto

                comando2 = """INSERT INTO carrinho (id_produto, id_cliente, nome, descricao, quantidade, preco)
                            VALUES(?,?,?,?,?,?)"""

                dados = (
                    id,
                    id_cliente,
                    nome,
                    descricao,
                    quantidade_produto,
                    calculando_preco,
                )

                cur.execute(comando2, dados)
                con.commit()

                print("Item adicionado ao carrinho com sucesso!")
            else:
                print("Quantidade selecionada maior que disponível.")

            cur.execute(comando2, dados)
            con.commit()

            print("Item adicionado ao carrinho com sucesso!")
        else:
            print("Produto não encontrado!")
