import math

testes=int(input())

for i in range(testes):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    
    lado1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    lado2 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    lado3 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

    semiperimetro = (lado1 + lado2 + lado3) / 2

    area= math.sqrt(semiperimetro * (semiperimetro-lado1) * (semiperimetro-lado2) * (semiperimetro-lado3))

    print('%.3f'%area)