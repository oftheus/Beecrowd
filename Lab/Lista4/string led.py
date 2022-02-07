N, L = map(int, input().split())
#N => nº de segmentos
#L => nº de ligações (linhas)
lista=[N,L]
k=(lista[1])
q=0
jesuslista=[]

for j in range(0,k):
    q==k
    lista2=list(map(int, input().split()))
    jesuslista.extend(lista2)

#bosslista = sorted(jesuslista)
#z=len(bosslista) #quantidade de termos
#NumeroFinal=bosslista[len(bosslista)-1]
#z=NumeroFinal

#if ((bosslista.count(bosslista[0]))>=2) or ((bosslista.count(bosslista[z]))>=2):
    #print("COMPLETO")
#else:
    #print("INCOMPLETO")

#só é completo se o último ou o primeiro termo da lista aparecem 2 vezes ou mais