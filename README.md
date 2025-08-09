# Sistema de Vendas Simples em Python

Este é um projeto simples de sistema de vendas e gerenciamento de estoque, desenvolvido em Python como parte de um exercíciodo curso. O objetivo é simular as operações básicas de um e-commerce em um ambiente de console, utilizando o banco de dados SQLite3 para armazenar os dados.

## Funcionalidades

O sistema oferece dois painéis de acesso principais:

### 1. Painel Administrativo

Este painel é acessado com um login e senha pré-definidos e permite ao administrador gerenciar o sistema de estoque e vendas.

* **Listar Produtos:** Visualizar todos os produtos cadastrados com suas informações.
* **Atualizar Estoque:** Mudar a quantidade de um produto no estoque.
* **Deletar Produtos:** Remover produtos do catálogo.
* **Relatórios de Vendas:** Acessar um relatório com o histórico de vendas realizadas.

### 2. Painel do Cliente

Este painel permite que os clientes interajam com a loja virtual para realizar compras.

* **Login e Cadastro:** Os clientes podem fazer login com seu e-mail ou se cadastrar caso ainda não tenham uma conta.
* **Seleção de Produtos:** Visualizar os produtos disponíveis e adicioná-los a um carrinho de compras.
* **Finalizar Compra:** Concluir a compra, que registra a venda e esvazia o carrinho.

## Estrutura do Projeto

O projeto é dividido em módulos, cada um com uma responsabilidade específica:

* `main.py`: O ponto de entrada do programa. Responsável por exibir os menus principais e gerenciar o fluxo de navegação entre o painel de admin e o de cliente.
* `estoque.py`: Contém as classes e funções para gerenciar o estoque e os produtos, como `Produto`, `listar_produtos`, `atualizar_quantidade`, etc.
* `vendas.py`: Contém a lógica de vendas e carrinho de compras, incluindo a classe `Venda` e as funções `selecionar_produto` e `finalizar_compra`.
* `register.py`: Gerencia o cadastro e o login dos clientes, com funções como `cadastro`, `verificar_login` e `verificar_email`.
* `db.py`: Centraliza a conexão com o banco de dados SQLite3, tornando-o acessível aos outros módulos.

## Como Executar

Para rodar o projeto, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    ```

2.  **Entre na pasta do projeto:**
    ```bash
    cd nome-do-seu-projeto
    ```

3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```

O programa irá iniciar no terminal e você poderá interagir com os menus.

## Tecnologias Utilizadas

* Python 3
* Módulo `sqlite3` para gerenciamento do banco de dados.

---
