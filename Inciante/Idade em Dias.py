idade_dias=int(input())
anos=idade_dias//365
if anos==0:
    meses=idade_dias//30
elif anos !=0:
    meses=(idade_dias - anos*365)//30

if meses==0:
    dias=idade_dias
elif meses!=0:
    dias=(idade_dias - anos*365 - meses*30)

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")