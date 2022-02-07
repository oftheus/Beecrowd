n = int(input())

listapar=[]
listaimpar = []
listafinal = []

for i in range(n):
    x=int(input())
    if x%2==0 or x==0:
        listapar.append(x)
    else:
        listaimpar.append(x)       

listapar.sort()

listaimpar.sort(reverse=True)

listafinal = listapar + listaimpar

for i in range(n):
    print(listafinal[i])