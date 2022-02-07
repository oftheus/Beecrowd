qpinos, alt = list(map(int, input().split()))
pinos = list(map(int, input().split()))
movi = 0
for i in range(qpinos-1):
    movi+=abs(pinos[i]-alt)
    pinos[i+1]+=alt-pinos[i]    
    pinos[i] = alt
print(movi)