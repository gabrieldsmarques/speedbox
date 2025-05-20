from datetime import datetime

class Movimentacao:
    def __init__(self, data_hora: datetime, localizacao: str, descricao: str):
        self.data_hora = data_hora
        self.localizacao = localizacao
        self.descricao = descricao
