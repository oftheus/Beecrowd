carta_a, carta_b = list(map(int, input().split()))

if (carta_a == carta_b):
    print(f'{carta_a}')
elif (carta_a > carta_b):
    print(f'{carta_a}')
elif (carta_a < carta_b):
    print(f'{carta_b}')