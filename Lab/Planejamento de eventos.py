pessoas,orcamento,hoteis,semanas=map(int,input().split())
soma=3000000
for c in range(hoteis):
    preco=int(input()) #para uma pessoa em um fds
    camas=sorted(list(map(int,input().split())))
    custo=pessoas*preco
    if custo<=orcamento and custo<=soma and any(x in camas for x in range(pessoas,1000)): #camas disponiveis
        soma=custo
if soma==3000000:
    print('stay home')
else:
    print(soma)