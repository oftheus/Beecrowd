a,b,c=map(float,input().split())
delta=b**2-4*a*c
if 2*a==0 or delta<0:
    print("Impossivel calcular")
else:
    formula1=((-b+(delta)**(1/2))/(2*a))
    formula2=((-b-(delta)**(1/2))/(2*a))
    print("R1 =","%.5f"%formula1)
    print("R2 =","%.5f"%formula2)
