class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    def login(self):
        print(f"Usuário {self.nome} logado.")

    def visualizar_historico(self):
        pass  # Implementação posterior
