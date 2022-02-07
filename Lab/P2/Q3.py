cifra = input()
palavra = input()

quantidade = 0
tam_palavra = len(palavra)
tam_cifra = len(cifra)

for i in range(0, (tam_cifra-tam_palavra) + 1):
    nova_cifra = cifra[i:i + tam_palavra]

    for j in range(tam_palavra):
        flag = True
        if palavra[j] == nova_cifra[j]:
            flag = False
            break
    
    quantidade += 1 if flag else 0
        

print(quantidade)

