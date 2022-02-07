peca1,npeca1,vpeca1 = map(float,input().split())
peca2,npeca2,vpeca2 = map(float,input().split())
valor = npeca1*vpeca1 + npeca2*vpeca2
print("VALOR A PAGAR: R$", "%.2f"%valor)