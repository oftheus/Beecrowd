chocadeiras, frangos = list(map(int, input().split()))
intervalos = list(map(int, input().split()))
#max_intervalos = frangos

def matriz_de_chocadeiras(dias):
    # instancia a matriz de elementos
    max_intervalos = dias
    matriz = [None] * chocadeiras
    for idx, intervalo in enumerate(intervalos):    
        uso = [0] * max_intervalos
        for i in range(intervalo-1, max_intervalos, intervalo):
            uso[i] = 1    
        matriz[idx] = uso    

    return matriz

# procura o dia em que a quantidade foi atingida
dias = 1
original = matriz_de_chocadeiras(dias)

img = [None] * (1 + chocadeiras)
img[0] = [0] * (1 + dias)
for lin in range(1, chocadeiras+1):
    img[lin] = [0] * (1 + dias)
    for col in range(1, dias + 1):
        img[lin][col] = img[lin][col-1] + img[lin-1][col] - img[lin-1][col-1] + original[lin-1][col-1]

while(img[-1][dias] < frangos):
    dias += 1
    original = matriz_de_chocadeiras(dias)
    img = [None] * (1 + chocadeiras)
    img[0] = [0] * (1 + dias)
    for lin in range(1, chocadeiras+1):
        img[lin] = [0] * (1 + dias)
        for col in range(1, dias + 1):
            img[lin][col] = img[lin][col-1] + img[lin-1][col] - img[lin-1][col-1] + original[lin-1][col-1]
    

print(dias)