n1,n2,n3,n4=map(float,input().split())
media=(n1*2+n2*3+n3*4+n4*1)/10
if media>=7.0:
    print("Media:",media)
    print("Aluno aprovado.")
elif media>=5.0 and media<=6.9:
    q=float(input())
    m=(q+media)/2
    print("Media:",media)
    print("Aluno em exame.")
    print("Nota do exame:",q)
    if m>=5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:","%.1f"%(m))
else:
    print("Media:","%.1f"%media)
    print("Aluno reprovado.")
    