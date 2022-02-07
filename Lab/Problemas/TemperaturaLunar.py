testes = 0
medicoes, intervalo = list(map(int, input().split()))
while(medicoes != 0 or intervalo != 0):
    testes += 1
    acumulado = [0]
    for i in range(medicoes):
        temperatura = int(input())
        acumulado.append(acumulado[i] + temperatura)

    medias = []
    for j in range((medicoes-intervalo)+1):
        media = (acumulado[j + intervalo] - acumulado[j])/intervalo
        medias.append(media)

    print(f'Teste {testes}')
    print(f'{int(min(medias))} {int(max(medias))}')
    print()
    medicoes, intervalo = list(map(int, input().split()))

