
class Clientes:
    def __init__(self, nome, telefone, email, ID ):
        self.nome = nome
        self.telefone = telefone 
        self.email = email
        self.ID = ID

    def __str__(self):
        return f'{self.nome} (Telefone: {self.telefone} | Email: {self.email})'
    
class Quarto:
    def __init__(self, numero,tipo , preco):
        self.numero = numero
        self.preco = preco 
        self.tipo = tipo
        self.ocupado = False
        
    def __str__(self):
        status = 'Ocupado' if self.ocupado else 'Disponivel'
        return f' Quarto: {self.numero} - {self.tipo} - {self.preco} - {status}'
    
class Reservas:
    def __init__(self, cliente, quarto, data_entrada, data_saida):
        self.cliente = cliente
        self.quarto = quarto
        self.data_entrada = data_entrada 
        self.data_saida = data_saida
    
    def __str__(self):
        return f'Reserva {self.cliente.nome} no Quarto: {self.quarto} de {self.data_entrada} a {self.data_saida}'
    

class Gerenciador:
    def __init__(self):
        pass
    
