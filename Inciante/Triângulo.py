x,y,z=map(float,input().split())
if x+y>z and z+y>x and x+z>y:
    p=x+y+z
    print("Perimetro = ""%.1f"%p)
else:
    a=((x+y)*z)/2
    print("Area = ""%.1f"%a)
    