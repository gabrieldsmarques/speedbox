class MeioTransporte:
    def __init__(self, tipo: str, velocidade_media: float, custo_por_km: float, alcance_maximo: float):
        self.tipo = tipo
        self.velocidade_media = velocidade_media
        self.custo_por_km = custo_por_km
        self.alcance_maximo = alcance_maximo
