import math

tam_vermelho = int(input(), base=16)
tam_verde = int(input(), base=16)
tam_azul = int(input(), base=16)

quantidade_verdes = (math.floor(tam_vermelho / tam_verde))**2
quantidade_azuis_para_cada_verde = (math.floor(tam_verde / tam_azul))**2

total = 1 + quantidade_verdes + (quantidade_azuis_para_cada_verde * quantidade_verdes)

print(hex(total)[2:])