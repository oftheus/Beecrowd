num_secoes = int(input())
secoes = list(map(int, input().split()))

posterior = sum(secoes)
acumulador = 0

for i in range(num_secoes):
    acumulador += secoes[i]
    posterior -= secoes[i]

    if(acumulador == posterior):
        print(i+1)
        break
