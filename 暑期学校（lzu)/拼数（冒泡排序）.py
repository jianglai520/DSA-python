n = int(input())
nums = input().split()

for i in range(n-1):
    for j in range(n-i-1):
        if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("".join(nums))