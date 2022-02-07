from math import sqrt

def eh_primo(numero):

    prime_flag = 0
 
    if(numero > 1):
        for i in range(2, int(sqrt(numero)) + 1):
            if (numero % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

entrada = int(input())

while(1):
    try:

        if(eh_primo(entrada)):
            valor = entrada
            
            while(valor != 0):
                digito = 10
                ultimo_digito = valor % 10
                if(eh_primo(ultimo_digito)):
                    valor = int(valor/digito)
                    digito *= 10
                else:
                    print('Primo')
                    break

            if(int(valor) == 0):
                print('Super')
        else:
            print('Nada')

        entrada = int(input())
    
    except EOFError:
        break