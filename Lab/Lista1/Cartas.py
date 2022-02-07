def EncontraOrdem(cartas):
    
    if (len(cartas) == 1):
        return None

    ordemAnterior = EncontraOrdem(cartas[1:])

    ordem = None
    if (cartas[0] > cartas[1]):
        ordem = 'D'
    elif (cartas[0] < cartas[1]):
        ordem = 'C'

    
    if(ordemAnterior == ordem or ordemAnterior == None):
        return ordem
    else:
        return 'N'



cartas = list(map(int, input().split()))
ordem = EncontraOrdem(cartas)
print(f"{ordem}")

