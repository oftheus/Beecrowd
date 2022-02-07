p=3.14159
pi=float(p)
A,B,C=map(float,input().split())
atriangulo = (A*C)/2
acirculo   = (pi*C**2)
atrapezio  = ((A+B)*C)/2
aquadrado  = (B**2)
aretangulo = (A*B)

print("TRIANGULO:","%.3f"%atriangulo)
print("CIRCULO:","%.3f"%acirculo)
print("TRAPEZIO:","%.3f"%atrapezio)
print("QUADRADO:","%.3f"%aquadrado)
print("RETANGULO:","%.3f"%aretangulo)
