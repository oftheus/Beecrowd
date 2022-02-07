def mdc(num1, num2):
    resto = None
    while resto != 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1

a, b, c, d = list(map(int, input().split())) 

num = a*d + c*b
den = b*d

mdc_num_den = mdc(num, den)

if (mdc_num_den == 1):
    print(f'{int(num)} {int(den)}')    
else:
    print(f'{int(num/mdc_num_den)} {int(den/mdc_num_den)}')