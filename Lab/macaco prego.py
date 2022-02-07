t=1
n = int(input()) 
while n!=0:

#se for só um retangulo
    if n==1:
        x1,y1,x2,y2 = map(int,input().split())
        print("Teste",t)
        print(x1,y1,x2,y2)
        print()
        t+=1

#saber se tem interseção ou não entre 2
    
    if n!=1:

        x1,y1,x2,y2 = map(int,input().split())
        x3,y3,x4,y4 = map(int,input().split())

        x5 = max(x1, x3)
        y5 = min(y1, y3)

        x6 = min(x2, x4)
        y6 = max(y2, y4)

#caso não tenha interseção
    if n==2:
        if (x5 > x6 and y5 > y6 or x5 < x6 and y5 < y6) :
            print("Teste",t)
            print("nenhum")
            print()
            t+=1

#caso tenha interseção
        else:
            print("Teste",t)
            print(x5,y5,x6,y6)
            print()
            t+=1

#interseção entre 3 ou mais
    
    if n>=3:
        for i in range(n-2):
            x7,y7,x8,y8 = map(int,input().split())
            x10 = max(x5, x7)
            y10 = min(y5, y7)
            x11 = min(x6, x8)
            y11 = max(y6, y8)
            
            x5=x10
            y5=y10
            x6=x11
            y6=y11
           
        if ((x10) >= abs(x11) and abs(y10) >= abs(y11) or x10 < abs(x11) and y10 < y11) :
            print("Teste",t)
            print("nenhum")
            print()
            t+=1
        else:
            print("Teste",t)
            print(x10,y10,x11,y11)
            print()
            t+=1
                
    n = int(input())