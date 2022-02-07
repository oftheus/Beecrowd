maior_representavel = int(input())
operando_1, operacao, operando_2 = input().split()

resultado = None

if (operacao == '*'):
    resultado = int(operando_1) * int(operando_2)
elif (operacao == '+'):
    resultado = int(operando_1) + int(operando_2)

if(resultado <= maior_representavel):
    print(f'OK')
else:
    print(f'OVERFLOW')