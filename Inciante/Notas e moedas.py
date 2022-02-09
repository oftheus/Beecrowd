x=float(input())
q=x//100
c=(x-(q*100))//50
v=(x-(c*50)-(q*100))//20
d=(x-(v*20)-(c*50)-(q*100))//10
f=(x-(d*10)-(v*20)-(c*50)-(q*100))//5
g=(x-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//2

u=(x-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//1
a=(x-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//(0.5)
b=(x-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//(0.25)
e=(x-(b*0.25)-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//(0.10)
h=(x-(e*0.10)-(b*0.25)-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//0.05
l=(x-(h*0.05)-(e*0.10)-(b*0.25)-(a*0.5)-(u)-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//0.01

print("NOTAS:")
print(int(q),"nota(s) de R$ 100.00")
print(int(c),"nota(s) de R$ 50.00")
print(int(v),"nota(s) de R$ 20.00")
print(int(d),"nota(s) de R$ 10.00")
print(int(f),"nota(s) de R$ 5.00")
print(int(g),"nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(u),"moeda(s) de R$ 1.00")
print(int(a),"moeda(s) de R$ 0.50")
print(int(b),"moeda(s) de R$ 0.25")
print(int(e),"moeda(s) de R$ 0.10")
print(int(h),"moeda(s) de R$ 0.05")
print(int(l),"moeda(s) de R$ 0.01")