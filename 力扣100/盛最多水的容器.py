"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                avaiable_area = (j - i) * min(height[i], height[j])
                max_area = max(avaiable_area, max_area)

        return max_area

# 超出时间限制，时间复杂度O(n**2)






