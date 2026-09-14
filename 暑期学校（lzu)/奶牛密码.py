st, N = input().split()
n = int(N)
nums = len(st)

while nums < n:
    st += (st[-1] + st[0:nums])
    nums = len(st)

print(st[n-1])