# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
# 示例
# 2：
#
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
# 示例
# 3：
#
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]


# 暴力枚举
from typing import List

def twosum(nums: List[int], target: int) -> List[int] | None:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twosum([1, 2, 4], 6))
