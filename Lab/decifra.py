c=input()
f=input()
a='abcdefghijklmnopqrstuvwxyz'
saida=[]
for i in f:
    ind=a.index(i)
    saida.append(c[ind])
print(''.join(saida))