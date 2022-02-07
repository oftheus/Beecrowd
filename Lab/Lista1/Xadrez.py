linhas = int(input())
colunas = int(input())

cor = True

for _ in range(linhas - 1):
    cor = not cor

for _ in range(colunas - 1):
    cor = not cor

valor = 1 if cor else 0

print(f"{valor}")

