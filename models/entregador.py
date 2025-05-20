from models.usuario import Usuario

class Entregador(Usuario):
    def __init__(self, id: int, nome: str, email: str, meio_transporte):
        super().__init__(id, nome, email)
        self.meio_transporte = meio_transporte

    def atualizar_status_entrega(self, status: str):
        print(f"Status da entrega atualizado para: {status}")
