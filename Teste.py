class GerenciamentoReserva:
    def __init__(self):
        self.reservas = []

    def fazer_reserva(self, cliente, quarto, data_entrada, data_saida):
        if not quarto.ocupado:
            reserva = Reserva(cliente, quarto, data_entrada, data_saida)
            quarto.ocupado = True
            self.reservas.append(reserva)
            print("Reserva feita com sucesso!")
        else:
            print("Erro: Quarto já está ocupado.")

    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva cadastrada.")
        for reserva in self.reservas:
            print(reserva)

    def cancelar_reserva(self, cliente_nome):
        for reserva in self.reservas:
            if reserva.cliente.nome == cliente_nome:
                reserva.quarto.ocupado = False
                self.reservas.remove(reserva)
                print("Reserva cancelada com sucesso!")
                return
        print("Reserva não encontrada.")
