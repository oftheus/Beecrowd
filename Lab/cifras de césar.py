def cesar(entrada,h):
	saida=""
	for c in range(len(entrada)):
		letra = entrada[c]
		if (letra.isupper()):
			saida = saida + chr((ord(letra) + h-65) % 26 + 65)
		else:
			saida = saida + ((ord(letra) + h - 97) % 26 + 97)
	return saida

casos=int(input())
for i in range(casos):
    entrada = input()
    deslocamento = -(int(input()))
    print(cesar(entrada,deslocamento))