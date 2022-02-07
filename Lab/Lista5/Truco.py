rodadas = int(input())

ordem_cartas = [4,5,6,7,12,11,13,1,2,3]
partidas_adalberto = 0
partidas_bernadete = 0

for _ in range(rodadas):
    jogadas = list(map(int, input().split()))
    jogadas_adalberto = jogadas[:3]
    jogadas_bernardete = jogadas[3:]
    pontos_adalberto = 0
    pontos_bernadete = 0

    # para cada rodada da partida
    for i in range(3):
        if  ordem_cartas.index(jogadas_adalberto[i]) >= ordem_cartas.index(jogadas_bernardete[i]):
            pontos_adalberto += 1
        else:
            pontos_bernadete += 1

    if(pontos_adalberto >= pontos_bernadete):
        partidas_adalberto += 1
    else:
        partidas_bernadete += 1
    


print(f'{partidas_adalberto} {partidas_bernadete}')

    