from models.meio_transporte import MeioTransporte

class Bicicleta(MeioTransporte):
    def __init__(self):
        super().__init__('Bicicleta', 15.0, 0.2, 10.0)

class Moto(MeioTransporte):
    def __init__(self):
        super().__init__('Moto', 40.0, 0.5, 50.0)

class Carro(MeioTransporte):
    def __init__(self):
        super().__init__('Carro', 60.0, 0.7, 100.0)

class Drone(MeioTransporte):
    def __init__(self):
        super().__init__('Drone', 30.0, 0.8, 20.0)
