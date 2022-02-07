from collections import deque

pesos = int(input())

lado_a = list(map(int, input().split()))
lado_a.sort()
lado_a = deque(lado_a)
lado_b = deque([])

consegueLevar = 'S'
while(len(lado_a) != 0):
    min_a = min(lado_a)
    if(lado_a[0] <= 8):
        lado_b.append(lado_a.popleft())
    elif(lado_a[0] > 8 and (len(lado_b) > 0 and lado_a[0]-min(lado_b) <= 8)):
        min_b = min(lado_b)
        lado_a.append(min_b)
        lado_b.remove(min_b)
        lado_b.append(lado_a.popleft())
    else:
        consegueLevar = 'N'
        break

print(consegueLevar)