apples = list(map(int, input().split()))
height = int(input())

max_height = height + 30
count = 0

for apple in apples:
    if max_height >= apple:
        count += 1

print(count)
