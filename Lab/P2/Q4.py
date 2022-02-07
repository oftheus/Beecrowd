from math import gcd
from functools import reduce

def mdc(list):
    x = reduce(gcd, list)
    return x

chocadeiras, frangos = list(map(int, input().split()))
intervalos = list(map(int, input().split()))

intervalos_vs_frangos = [x * frangos for x in intervalos]
max_intervalos = mdc(intervalos_vs_frangos)

# instancia a matriz de elementos
matriz = [None] * chocadeiras
for idx, intervalo in enumerate(intervalos):    
    uso = [0] * max_intervalos
    for i in range(intervalo-1, max_intervalos, intervalo):
        uso[i] = 1    
    matriz[idx] = uso


# instancia a matriz imagem integral
img = [None] * (1 + chocadeiras)
img[0] = [0] * (1 + max_intervalos)
for lin in range(1, chocadeiras+1):
    img[lin] = [0] * (1 + max_intervalos)
    for col in range(1, max_intervalos + 1):
        img[lin][col] = img[lin][col-1] + img[lin-1][col] - img[lin-1][col-1] + matriz[lin-1][col-1]

# procura o dia em que a quantidade foi atingida
i = 1
while(img[-1][i] < frangos):
    i += 1

print(i)