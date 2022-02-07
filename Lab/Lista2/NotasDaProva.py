nota = int(input())

mapeamento = {
    (lambda x: 86 <= x <= 100): 'A', 
    (lambda x: 61 <= x <= 85): 'B',
    (lambda x: 36 <= x <= 60): 'C',
    (lambda x: 1 <= x <= 35): 'D',
    (lambda x: x == 0): 'E'
}

for func in mapeamento:
    if func(nota):
        print(f'{mapeamento[func]}')
        break