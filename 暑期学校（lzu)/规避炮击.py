n = int(input())
attacks = []

for i in range(n):
    a, b, g, k = map(int, input().split())
    attacks.append((a, b, a + g, b + k))

x, y = map(int, input().split())

for i in range(n-1,-1,-1):
    x1, y1, x2, y2 = attacks[i]
    if x1 <= x <= x2 and y1 <= y <= y2:
        print(i+1)
        break
else:
    print(-1)