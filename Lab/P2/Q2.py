pesos = int(input())

lado_a = list(map(int, input().split()))

for i in range(1, pesos):
    lado_a.sort()

    if (lado_a[0] > 8):
        print("N")
        exit()
    elif (lado_a[i] - lado_a[i-1] > 8):
        print("N")
        exit()

print('S')