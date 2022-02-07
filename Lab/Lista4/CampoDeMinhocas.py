lin, col = list(map(int, input().split()))

matriz_de_minhocas = []

for _ in range(lin):
    linha = list(map(int, input().split()))
    matriz_de_minhocas.append(linha)

# calcula maximo das linhas    
maior_linha = max(
    sum(linha) for linha in matriz_de_minhocas
)

# transpoe matriz
transposta = [[matriz_de_minhocas[j][i] for j in range(len(matriz_de_minhocas))] for i in range(len(matriz_de_minhocas[0]))]


maior_coluna = max(
    sum(coluna) for coluna in transposta
)

print(max(maior_coluna, maior_linha))