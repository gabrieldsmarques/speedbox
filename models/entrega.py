from models.movimentacao import Movimentacao

class Entrega:
    def __init__(self, id: int, cliente, entregador, origem: str, destino: str):
        self.id = id
        self.cliente = cliente
        self.entregador = entregador
        self.origem = origem
        self.destino = destino
        self.status = 'Pendente'
        self.historico_movimentacao = []

    def calcular_tempo_estimado(self, distancia: float) -> float:
        return distancia / self.entregador.meio_transporte.velocidade_media

    def registrar_movimentacao(self, movimentacao: Movimentacao):
        self.historico_movimentacao.append(movimentacao)
