num_postos, distancia_intermediaria_max = list(map(int, input().split()))
postos = list(map(int, input().split()))

consegue_terminar = True
for i in range(num_postos - 1):
    diff = postos[i + 1] - postos[i]
    if (diff > distancia_intermediaria_max):
        consegue_terminar = False
        break

diff_ate_o_final = 42195 - postos[-1]

if (diff_ate_o_final > distancia_intermediaria_max):
    consegue_terminar = False
    

if consegue_terminar:
    print('S')
else:
    print('N')


