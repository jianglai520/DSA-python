"""
算法：哈希映射
时间复杂度：O(n)
空间复杂度：O(n)
拿到题目先问四个问题：
1）数组有序吗？有序-->优先双指针；无序 --> 哈希表 or 先排序
2）要返回什么？返回下标，不能排序（会丢失原始位置），只能哈希表；返回数值/组合/是否存在，可以排序
3）要不要所有不重复解？要的话排序 + 双指针 + 跳过重复元素
4）是“两数”还是“子数组/子串”？子数组的话前缀和  + 哈希表；子串的话用滑动窗口/前缀和
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable = dict()

    for i, num in enumerate(nums):
        if (target - num) in hashtable:
            return [i, hashtable[target - num]]
        hashtable[num] = i
    return []

# 测试
if __name__ == "__main__":
    nums = [1, 3, 5]
    target = 4
    print(twoSum(nums, target))



