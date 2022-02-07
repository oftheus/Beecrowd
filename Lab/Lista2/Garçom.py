bandejas = int(input())

copos_quebrados = 0

for i in range(bandejas):
    latas, copos = list(map(int, input().split()))
    copos_quebrados += copos if latas > copos else 0

print(f'{copos_quebrados}')
