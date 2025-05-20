from models.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id: int, nome: str, email: str, endereco: str):
        super().__init__(id, nome, email)
        self.endereco = endereco

    def solicitar_entrega(self):
        print(f"{self.nome} solicitou uma nova entrega.")
