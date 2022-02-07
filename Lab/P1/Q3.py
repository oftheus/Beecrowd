valores = list(map(int, input().split()))

def Verifica_Retorno(a, b):
    if((a + b) == 0):
        return True
    elif ((a + (-b)) == 0):
        return True
    elif (((-a) + b) == 0):
        return True
    elif (((-a)+(-a)) == 0):
        return True
    else:
        return False

def Verifica_Retorno_Tres_Digitos(a, b, c):
    if((a + b + c) == 0):
        return True
    elif ((a + b + (-c)) == 0):
        return True
    elif ((a + (-b) + c) == 0):
        return True
    elif ((a + (-b) + (-c)) == 0):
        return True
    elif (((-a) + b + c) == 0):
        return True
    elif (((-a) + b + (-c)) == 0):
        return True
    elif (((-a) + (-b) + c) == 0):
        return True
    elif (((-a) + (-b) + (-c)) == 0):
        return True
    else:
        return False


a = Verifica_Retorno(valores[0], valores[1])
b = Verifica_Retorno(valores[1], valores[2])
c = Verifica_Retorno(valores[0], valores[2])
d = Verifica_Retorno_Tres_Digitos(valores[0], valores[1], valores[2])

if (a==True or b==True or c==True or d==True):
    print(f"S")
else:
    print(f"N")


    