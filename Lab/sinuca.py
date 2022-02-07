import math

n_bolas=int(input())
l=list(map(int,input().split()))
num=math.ceil(n_bolas/2)
novo=[]
x=len(l)
t=1

for j in range(num):
    for c in range(x-t):
        if l[c]+l[c+1]==2:
            novo.append(1)
        elif l[c]+l[c+1]==-2:
            novo.append(1)
        else:
            novo.append(-1)
    del l[:]
    t+=1
    if len(novo)==1:
        if novo[0]==1:
            print('preta')
        else:
            print('branca')        
        break
    
    for i in range(x-t):
        if novo[i]+novo[i+1]==2:
            l.append(1)
        elif novo[i]+novo[i+1]==-2:
            l.append(1)
        else:
            l.append(-1)
    del novo[:]
    t+=1
    if len(l)==1:
        if l[0]==1:
            print('preta')
        else:
            print('branca') 
        break