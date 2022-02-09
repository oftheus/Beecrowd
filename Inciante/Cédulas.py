x=int(input())
q=x//100
c=(x-(q*100))//50
v=(x-(c*50)-(q*100))//20
d=(x-(v*20)-(c*50)-(q*100))//10
f=(x-(d*10)-(v*20)-(c*50)-(q*100))//5
g=(x-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//2
u=(x-(g*2)-(f*5)-(d*10)-(v*20)-(c*50)-(q*100))//1
print(x)
print(q,"nota(s) de R$ 100,00")
print(c,"nota(s) de R$ 50,00")
print(v,"nota(s) de R$ 20,00")
print(d,"nota(s) de R$ 10,00")
print(f,"nota(s) de R$ 5,00")
print(g,"nota(s) de R$ 2,00")
print(u,"nota(s) de R$ 1,00")
