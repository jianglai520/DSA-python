from typing import List

def findDuplicate(nums: List[int]) -> int:
    set1 = set()
    set2 = set()

    for num in nums:
        if num not in set1:
            set1.add(num)
        else:
            set2.add(num)
    return list(set2)[0]

print(findDuplicate([1, 2, 4, 2, 2]))    # 空间复杂度不是常数--pass