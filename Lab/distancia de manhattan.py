x_maria, y_maria, x_reuniao, y_reuniao = list(map(int, input().split()))
#abs para retornar o valor absoluto do nº
diferenca_entre_xs = abs(x_maria - x_reuniao) 
diferenca_entre_ys = abs(y_maria - y_reuniao)

print(diferenca_entre_xs + diferenca_entre_ys)