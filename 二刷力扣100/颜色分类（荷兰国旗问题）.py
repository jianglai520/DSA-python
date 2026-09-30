"""
荷兰国旗问题（一遍遍历） -- 推荐
用三个指针 low mid high 把数组分成四个区间
[0, low]  -- 已经确定的0区
[low, mid]  -- 已经确定的1区
[mid, high]  -- 还没检查的区域
[high, n-1]  -- 已经确定的2区

数组样子（核心不变式）：
0 0 0 | 1 1 1 | ？ ？ ？ | 2 2 2

low 左边（不含） 全是0
low 到 mid之间（不含）全是1
mid 到 high 之间是待处理的未知区域
high右边（不含）全是2

我们只需要不断缩小 [mid, high]这个未知区域，直到它为空(mid > high)
"""
from typing import List

def sortColor(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


