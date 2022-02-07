chave = input()
frase = input()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
frase_descriptografada = []
for caractere in frase:
    indice = alfabeto.index(caractere)
    frase_descriptografada.append(chave[indice])

print(''.join(frase_descriptografada))