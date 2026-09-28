from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)

    if not nums:
        return 0

    curr_longest = 1
    last_longest = 1

    for i in range(0, n - 1):
        if nums[i] == nums[i+1]:
            continue
        elif nums[i] + 1 == nums[i+1]:
            curr_longest += 1
            last_longest = max(last_longest, curr_longest)
        else:
            curr_longest = 1
    return last_longest

# 测试
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))