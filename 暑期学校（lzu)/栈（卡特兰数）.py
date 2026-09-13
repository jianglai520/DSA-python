# 这道题目用到了自底向上的动态规划思想

n = int(input())
f = [0] * (n + 1)
f[0] = 1

for i in range(1, n+1):
    for k in range(1, i+1):
        f[i] += f[k-1] * f[i-k]

print(f[n])

