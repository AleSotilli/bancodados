import heapq
import random
import names

class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade

    def __lt__(self, other):
        return self.prioridade < other.prioridade

def criar_fila_prioridades():
    return []

def inserir_paciente(fila, paciente):
    heapq.heappush(fila, paciente)

def remover_paciente(fila):
    return heapq.heappop(fila)

def visualizar_fila(fila):
    fila.sort(key=lambda paciente: paciente.prioridade)

    for paciente in fila:
        print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Prioridade: {paciente.prioridade}")

def criar_fila_atendidos():
    return []

def gerar_simulacao(quantidade, prioridade_minima, prioridade_maxima):
    fila = criar_fila_prioridades()

    for i in range(quantidade):
        prioridade = random.randint(prioridade_minima, prioridade_maxima)
        nome = names.get_full_name()
        idade = random.randint(1, 100)
        paciente = Paciente(nome, idade, prioridade)
        inserir_paciente(fila, paciente)

    return fila

def main():
    menu = """
    1. Listar pacientes
    2. Atender paciente
    3. Listar 5 últimos pacientes
    4. Gerar simulação
    5. Sair
    """
    fila = criar_fila_prioridades()
    pacientes_atendidos = criar_fila_atendidos()

    while True:
        # Exibe o menu
        print(menu)

        # Lê a opção do jogador
        opcao = input("Digite a opção: ")

        # Trata a opção do jogador
        if opcao == "1":
            # Lista os pacientes na fila de prioridades
            visualizar_fila(fila)
        elif opcao == "2":
            # Verifica se a fila está vazia
            if fila:
                # Remove o paciente de maior prioridade

                paciente_atendidos.append(pacientes_atendido)
                paciente_atendido = remover_paciente(fila)

                print(f"Paciente atendido: {paciente_atendido.nome}")
        elif opcao == "3":
            # Verifica se o parâmetro é uma fila
            if isinstance(pacientes_atendidos, list):
                # Lista os 5 últimos pacientes chamados
                pacientes_atendidos = pacientes_atendidos[-5:]
                for paciente in pacientes_atendidos:
                    print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Prioridade: {paciente.prioridade}")
        elif opcao == "4":
            # Gera uma simulação de pacientes
            quant = int(input("Quantidade de pacientes: "))
            min = int(input("Prioridade mínima: "))
            max = int(input("Prioridade máxima: "))
            fila = gerar_simulacao(quant, min, max)
        elif opcao == "5":
            # Sai do jogo
            break

if __name__ == "__main__":
    main()
