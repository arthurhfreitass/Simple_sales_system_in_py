from db import con, cur
from datetime import datetime
from estoque import atualizar_quantidade
from register import pegar_nome_cliente


class Venda:
    def __init__(self, id_produto, quantidade, preco, data=None, id=None):
        self.id = id
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco = preco
        self.data = data or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def salvar_vendas(self, con, cur):
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

                estoque_atualizado = quantidade - quantidade_produto
                atualizar_quantidade(estoque_atualizado, id)

                cur.execute(comando2, dados)
                con.commit()
                print("Item adicionado ao carrinho com sucesso!")

            else:
                print("Quantidade selecionada maior que disponível.")

        else:
            print("Produto não encontrado!")


def finalizar_compra(id_cliente):
    comando = """SELECT * FROM carrinho WHERE id_cliente = ?"""
    cur.execute(comando, (id_cliente,))
    carrinho = cur.fetchall()
    nome_cliente = pegar_nome_cliente(id_cliente)

    print("---" * 15)
    print("             CARRINHO DE COMPRAS")
    print("---" * 15)
    print("Item | Produto           | Qtd      | Sub Total. ")
    print("-------------------------------------------------------")

    num = 1
    preco_final = 0

    for finalizar in carrinho:
        if finalizar:
            id, id_cliente, id_produto, nome, descricao, quantidade, preco = finalizar

            print(f"""Produto {num}: Nome: {nome} | Quantidade: {quantidade} | Preço: {preco}"""
                  )
            num += 1
            preco_final += preco
            print()
    print("---" * 15)
    print(f"TOTAL DO CARRINHO: R${preco_final:.2f}")
    print("---" * 15)

    print("     FINALIZAR COMPRA")
    print("---" * 15)
    print("1- Para concluir a compra.")
    print("2- Para cancelar a compra.")
    print()
    
    decisao = input("Selecione uma opção valida: ")

    if decisao in ("1", "2"):
        if decisao == "1":
            print("---" * 10)
            print(f"Pedido finalizado, {nome_cliente}!")
            print("Sua compra foi concluída com sucesso e em breve você receberá mais detalhes por e-mail.")
            print("Agradecemos a confiança e volte sempre!")
            print("---" * 10)
            
            for apagando_carrinho in finalizar:
                if apagando_carrinho:
                    cur.execute("DELETE FROM carrinho WHERE id_cliente = ? ", (id_cliente,))
                    venda = Venda(id_produto, quantidade, preco)
                    venda.salvar_vendas(con, cur)
                    con.commit()
            
        elif decisao == ("2"):
            print(f"Pedido finalizado, {nome_cliente}!")

            for apagando_carrinho in finalizar:
                if apagando_carrinho:
                    cur.execute("DELETE FROM carrinho WHERE id_cliente = ? ", (id_cliente,))
                    con.commit()
    else:
        print("Selecione uma opção valida.")
        print()