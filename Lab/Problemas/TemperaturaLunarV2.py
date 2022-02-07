testes = 0
medicoes, intervalo = list(map(int, input().split()))
while(medicoes != 0 or intervalo != 0):
    testes += 1
    acumulado = [0]
    leituras = []
    for i in range(medicoes):
        temperatura = int(input())
        acumulado.append(acumulado[i] + temperatura)
        leituras.append(temperatura)

    medias = []
    for j in range(intervalo, medicoes):
        media = (acumulado[j]  + leituras[j] - leituras[j-intervalo])/4
        medias.append(media)

    print(f'Teste {testes}')
    print(f'{int(min(medias))} {int(max(medias))}')
    print()
    medicoes, intervalo = list(map(int, input().split()))

