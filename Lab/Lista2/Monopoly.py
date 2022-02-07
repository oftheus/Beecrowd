dinheiro, operacoes = list(map(int, input().split()))


jogadores = {
    'D' : dinheiro,
    'E' : dinheiro,
    'F' : dinheiro
}

def handle_compra(jogador, valor_gasto):
    jogadores[jogador] -= int(valor_gasto)

def handle_venda(jogador, valor_gasto):
    jogadores[jogador] += int(valor_gasto)

def handle_aluguel(recebe, paga, valor_gasto):
    jogadores[recebe] += int(valor_gasto)
    jogadores[paga] -= int(valor_gasto)


for _ in range(operacoes):
    
    inputs = input().split()
    if (len(inputs) == 3):
        operacao, a, b = inputs
    elif (len(inputs) == 4):
        operacao, a, b, c = inputs

    if(operacao == 'C'):
        handle_compra(a, b)
    elif(operacao == 'V'):
        handle_venda(a, b)
    elif(operacao == 'A'):
        handle_aluguel(a, b, c)

dalia = jogadores['D']
eloi = jogadores['E']
felix = jogadores['F']
print(f'{dalia} {eloi} {felix}')