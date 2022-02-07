entradas = int(input())

for i in range(entradas):
    valor_1, valor_2 = input().split()    

    if(valor_1[-len(valor_2):] == valor_2):
        print('encaixa')
    else:
        print('nao encaixa')

