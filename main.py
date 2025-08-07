from estoque import Produto, listar_produtos, atualizar_quantidade, deletar_produto, verificar_produto
from vendas import Venda, selecionar_produto
from register import Clientes, cadastro, verificar_login, verificar_email


while True:
    print("---" * 6)
    print("  WebSite Vendas")
    print("---" * 6)
    print("Selecione uma opção:")
    print("1- Painel Admin")
    print("2- Painel Cliente")
    print("3- Fechar Programa")
    
    opcao_principal = input("Selecione uma opção: (1, 2 ou 3)  ")

    if opcao_principal == "3":
        print("Encerrando o programa...")
        break

    if opcao_principal in ("1", "2"):
        if opcao_principal == "1":
            while True:
                print("---"* 6)
                print("Painel admin")
                print("---"* 6)
                print("1- Listar produtos cadastrados")
                print("2- Atualizar estoque")
                print("3- Deletar produtos")
                print("4- Voltar ao menu principal")

                opcao_admin = input("selecione uma opção:  ")

                if opcao_admin == "4":
                    break

                if opcao_admin == "1":
                    print("Listando os produtos cadastrados...")
                    print("")
                    listar_produtos()

                elif opcao_admin == "2":
                    quantidade_nova = int(input("Digite a quantidade do estoque do produto:  "))
                    id_produto = int(input("Digite o id do produto para atualizar:  "))

                    atualizar_quantidade(quantidade_nova, id_produto)
                    print()
                    print("Estoque atualizado com sucesso!")

                elif opcao_admin == "3":
                    id_produto = int(input("Qual o id do produto a ser excluido?  "))

                    deletar_produto(id_produto)
                    print()
                    print("Item deletado com sucesso!")

                else:
                    print()
                    print("ERRO: Selecione uma opção valida")
        
        elif opcao_principal == "2":
            while True:
                print("Login - webSite Vendas")
                print()
                nome = input("Digite seu nome corretamente:  ").strip().upper()

                email = input("Digite seu email: ").strip().upper()

                if verificar_login(email) == None:
                    if verificar_login(email) is None:
                        if verificar_email(email) and nome.strip() != "":
                            cadastro(nome, email)
                            print("Cadastro realizado com sucesso, realize o login para ser feliz...")
                            break
                        else:
                            print("Preencha corretamente todos os campos válidos.")
                            continue

                elif verificar_login(email) != None:
                    login = verificar_login(email)
                    while True:
                        print()
                        print("webSite Vendas")
                        print()
                        print("1-Selecionar produtos")
                        print("2- Finalizar compra")
                        print("3- Voltar ao menu principal")

                        opcao_vendas = input("Selecione uma opção")

                        if opcao_vendas == "4":
                            break

                        if opcao_vendas == "1":
                            listar_produtos()
                            print()
                            while True:
                                id = int(input("Selecione o produto: "))

                                resultado = verificar_produto(id)

                                if resultado:
                                    selecionar_produto(id, login)
                                    break
                                else:
                                    print("ERRO: Produto não cadastrado, tente novamente.")
                                    
        else:
           print()
           print("ERRO: Selecione uma opção valida")




        





