s, N = input().split()
n = int(N)
L0 = len(s)

L = L0
while L < n:
    L *= 2

while L > L0:
    half = L // 2
    if n <= half:
        pass
    elif n == half + 1:
        n = half
    else:
        n = n - half - 1
    L = half

print(s[n - 1])