from collections import deque

class Jogador:
    
    def __init__(self, id):
        self.id = id
        self.cartas = []

    def Pega_Carta(self, carta):
        self.cartas.append(carta)

    def Soma_Das_Cartas(self):
        return sum(self.cartas)

# lê entrada para jogadores, turnos e cartas
jogadores_e_turnos = list(map(int, input().split()))
num_jogadores = jogadores_e_turnos[0]
num_turnos = jogadores_e_turnos[1]

cartas = deque(list(map(int, input().split())))

# Cria uma instância de jogador para cada jogador lido
jogadores = [Jogador(i + 1) for i in range(num_jogadores)]

# para cada turno
    # para cada jogador 
        # jogador pega uma carta    
for i in range(num_turnos):
    for jogador in jogadores:
        jogador.Pega_Carta(cartas.popleft())


# decide quem ganhou o jogo
# ganha o jogo o jogador que tiver a maior somatória do numero de suas cartas
# variáveis sentinela
id_do_vencedor = 0
num_de_pontos_do_vencedor = 0

# para cada jogador faça
for jogador in jogadores:
    # calcula o número de pontos
    # compara com a sentinela, se for < ou = considerando que os jogadores estão em ordem
    # teremos o vencedor com mais pontos, ou, em caso de empate o último com maior quantidade de pontos
    num_de_pontos_atual = jogador.Soma_Das_Cartas()    
    if(num_de_pontos_do_vencedor <= num_de_pontos_atual):
        num_de_pontos_do_vencedor = num_de_pontos_atual
        id_do_vencedor = jogador.id

print(f"{id_do_vencedor}")