x=int(input())
horas=x//3600

if horas==0:
    minutos=x//60
elif horas !=0:
    minutos=(x-horas*3600)//60

segundos=x-horas*3600-minutos*60

print("{}:{}:{}".format(horas, minutos, segundos))