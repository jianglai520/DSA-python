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
def twosum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) + 1):
            if j < len(nums) and nums[i] + nums[j] == target and i != j:
                return [i, j]

print(twoSum([1, 2, 4], 6))
