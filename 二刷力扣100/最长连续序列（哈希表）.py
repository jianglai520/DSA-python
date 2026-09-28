from typing import List

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums_set = set(nums)
    last_longest = 1

    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            curr_longest = 1

            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_longest += 1

            last_longest = max(last_longest, curr_longest)
    return last_longest

# 测试
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))