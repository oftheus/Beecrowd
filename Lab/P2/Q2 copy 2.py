
from collections import deque
from itertools import product

pesos = int(input())

lado_a = list(map(int, input().split()))
lado_a = deque(lado_a)
lado_b = deque([])

consegueLevar = 'S'
while(len(lado_a) != 0):
    min_a = min(lado_a)
    if(min_a <= 8):
        lado_b.append(min_a)
        lado_a.remove(min_a)
        continue

    produtos = list(product(lado_a, lado_b))
    combinacoes_possiveis = list(filter(lambda e: abs(e[0] - e[1]) <= 8, produtos))
    if(len(combinacoes_possiveis) > 0):
        lado_a.append(combinacoes_possiveis[0][1])
        lado_b.append(combinacoes_possiveis[0][0])
        lado_b.remove(combinacoes_possiveis[0][1])
        lado_a.remove(combinacoes_possiveis[0][0])
        continue
    else:
        consegueLevar = 'N'
        break

print(consegueLevar)