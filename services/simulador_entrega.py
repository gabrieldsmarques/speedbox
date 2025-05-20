class SimuladorEntrega:
    def simular_tempo_entrega(self, distancia: float, meio_transporte) -> float:
        if distancia > meio_transporte.alcance_maximo:
            raise ValueError("Distância excede o alcance máximo do meio de transporte.")
        return distancia / meio_transporte.velocidade_media
