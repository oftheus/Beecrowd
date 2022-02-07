risada = input()

def removeCons(s):
    vogal = 'aeiou'
    nova_str=[]

    for x in s:
        if x in vogal:
            nova_str.append(x)
        
    s="".join(i for i in nova_str)
    return s

risada_sem_consoantes = removeCons(risada)

if(risada_sem_consoantes == risada_sem_consoantes[::-1]):
    print('S')
else:
    print('N')

