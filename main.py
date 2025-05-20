from models.cliente import Cliente
from models.entregador import Entregador
from models.subclasses_transporte import Moto, Carro, Bicicleta, Drone
from models.entrega import Entrega
from models.movimentacao import Movimentacao
from services.simulador_entrega import SimuladorEntrega
from datetime import datetime

clientes = []
entregadores = []
entregas = []

def carregar_dados_iniciais():
    
    clientes.append(Cliente(1, "Joana Prado", "joana@email.com", "Rua das Flores, 100"))
    clientes.append(Cliente(2, "Carlos Menezes", "carlos@email.com", "Av. Brasil, 2000"))

    entregadores.append(Entregador(1, "Rafaela Souza", "rafaela@email.com", Moto()))
    entregadores.append(Entregador(2, "Lucas Ferreira", "lucas@email.com", Carro()))
def escolher_transporte():
    print("Escolha o meio de transporte:")
    print("1 - Bicicleta")
    print("2 - Moto")
    print("3 - Carro")
    print("4 - Drone")
    opcao = input(">> ")
    if opcao == "1":
        return Bicicleta()
    elif opcao == "2":
        return Moto()
    elif opcao == "3":
        return Carro()
    elif opcao == "4":
        return Drone()
    else:
        print("Opção inválida. Padrão: Moto.")
        return Moto()

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    cliente = Cliente(len(clientes)+1, nome, email, endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso.")

def cadastrar_entregador():
    nome = input("Nome do entregador: ")
    email = input("Email: ")
    meio = escolher_transporte()
    entregador = Entregador(len(entregadores)+1, nome, email, meio)
    entregadores.append(entregador)
    print("Entregador cadastrado com sucesso.")

def solicitar_entrega():
    if not clientes or not entregadores:
        print("Cadastre ao menos um cliente e um entregador.")
        return

    print("Clientes disponíveis:")
    for i, c in enumerate(clientes):
        print(f"{i+1} - {c.nome}")
    cliente_idx = int(input("Escolha um cliente: ")) - 1

    print("Entregadores disponíveis:")
    for i, e in enumerate(entregadores):
        print(f"{i+1} - {e.nome} ({e.meio_transporte.tipo})")
    entregador_idx = int(input("Escolha um entregador: ")) - 1

    origem = input("Origem: ")
    destino = input("Destino: ")
    entrega = Entrega(len(entregas)+1, clientes[cliente_idx], entregadores[entregador_idx], origem, destino)
    entrega.registrar_movimentacao(Movimentacao(datetime.now(), origem, "Entrega iniciada"))
    entregas.append(entrega)
    print("Entrega cadastrada com sucesso.")

def simular_tempo_entrega():
    if not entregas:
        print("Nenhuma entrega registrada.")
        return

    for i, e in enumerate(entregas):
        print(f"{i+1} - {e.cliente.nome} → {e.destino} [{e.status}]")
    idx = int(input("Escolha a entrega: ")) - 1

    distancia = float(input("Informe a distância (km): "))
    simulador = SimuladorEntrega()
    try:
        tempo = simulador.simular_tempo_entrega(distancia, entregas[idx].entregador.meio_transporte)
        print(f"Tempo estimado de entrega: {tempo:.2f} horas")
    except ValueError as ve:
        print(f"Erro: {ve}")

def atualizar_status_entrega():
    if not entregas:
        print("Nenhuma entrega registrada.")
        return

    for i, e in enumerate(entregas):
        print(f"{i+1} - {e.cliente.nome} → {e.destino} [{e.status}]")
    idx = int(input("Escolha a entrega: ")) - 1

    novo_status = input("Novo status: ")
    local = input("Localização atual: ")
    entregas[idx].status = novo_status
    entregas[idx].entregador.atualizar_status_entrega(novo_status)
    entregas[idx].registrar_movimentacao(Movimentacao(datetime.now(), local, novo_status))

def visualizar_historico():
    
    if not entregas:
        print("Nenhuma entrega registrada.")
        return

    for i, e in enumerate(entregas):
        print(f"{i+1} - {e.cliente.nome} → {e.destino}")
    idx = int(input("Escolha a entrega: ")) - 1

    print("Histórico de movimentações:")
    for mov in entregas[idx].historico_movimentacao:
        print(f"[{mov.data_hora}] {mov.localizacao} - {mov.descricao}")

def listar_clientes():
    print("\nClientes cadastrados:")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    for c in clientes:
        print(f"ID {c.id}: {c.nome} - {c.email} - {c.endereco}")

def listar_entregadores():
    print("\nEntregadores cadastrados:")
    if not entregadores:
        print("Nenhum entregador cadastrado.")
    for e in entregadores:
        meio = e.meio_transporte.tipo
        print(f"ID {e.id}: {e.nome} - {e.email} - Veículo: {meio}")

def listar_transportes():
    print("\nMeios de Transporte disponíveis:")
    for t in [Moto(), Carro(), Bicicleta(), Drone()]:
        print(f"{t.tipo} | Velocidade: {t.velocidade_media} km/h | Custo/km: {t.custo_por_km} | Alcance: {t.alcance_maximo} km")

def menu():
    carregar_dados_iniciais()

    while True:
        print("\n=== MENU SPEEDBOX ===")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar entregador")
        print("3 - Solicitar entrega")
        print("4 - Simular tempo de entrega")
        print("5 - Atualizar status da entrega")
        print("6 - Visualizar histórico da entrega")
        print("7 - Listar clientes")
        print("8 - Listar entregadores")
        print("9 - Listar meios de transporte")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_entregador()
        elif opcao == "3":
            solicitar_entrega()
        elif opcao == "4":
            simular_tempo_entrega()
        elif opcao == "5":
            atualizar_status_entrega()
        elif opcao == "6":
            visualizar_historico()
        elif opcao == "7":
            listar_clientes()
        elif opcao == "8":
            listar_entregadores()
        elif opcao == "9":
            listar_transportes()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
