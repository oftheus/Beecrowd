carros, postos, tomadas = list(map(int, input().split()))

registros = []
posicoes = []

for _ in range(tomadas):
    carro, posto = list(map(int, input().split()))
    registros.append([carro, posto])

# remove registros invalidos
for carro in range(1, carros+1):
    pos = 1
    index_to_remove = []

    for i in range(len(registros)):  
        if(registros[i] == [carro, pos]):
            pos+=1

            if(pos > 4):
                pos = 1

        elif(registros[i][0] == carro and registros[i][1] != pos):
            index_to_remove.append(i)

    registros = [i for j, i in enumerate(registros) if j not in index_to_remove]


asd = [ [ 0 for i in range(2) ] for j in range(carros) ]
dsa = [ [ 0 for i in range(2) ] for j in range(carros) ]

for registro in range(len(registros)):
    carro = registros[registro][0]
    if (asd[carro-1][0] == carro):
        asd[carro-1][1] += 1
    else:
        asd[carro-1][0] = carro
        asd[carro-1][1] = 1

    dsa = asd
    dsa = sorted(dsa, key=lambda x: x[1], reverse=True)
    

posicoes = []
for car in dsa:
    posicoes.append(car[0])

print(' '.join(str(x) for x in posicoes))