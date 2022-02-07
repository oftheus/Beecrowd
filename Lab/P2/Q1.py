senhas = int(input())

for _ in range(senhas):
    senha = [s[0] for s in input().split()]
    print(str.join('', senha))

