casos = int(input()) #casos de testes

for q in range(0,casos):
    
    c = 0 #variável contadora
    VETOR = []
    primeirocaso = int(input())
    
    for q in range(0,primeirocaso):
        VETOR.append(input())
        
    for k in range(0,primeirocaso):
        if(VETOR[k] == 'RIGHT'):
            c=c+1
        elif(VETOR[k] == 'LEFT'):
            c=c-1
        else:
            VETOR[k] = VETOR[k].split()
            VETOR[k] = VETOR[k][len(VETOR[k])-1]
            VETOR[k] = VETOR[int(VETOR[k])-1]
            if(VETOR[k]=='LEFT'):
                c-=1
            else:
                c+=1
                
    print(c)