"""
Counter是python中 collections 模块里的一个类，专门用来计数。它本质是一个字典（dict的子类），key是元素，value是该元素出现的次数
"""

from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
count = Counter(nums)

print(count)    # Counter({1: 3, 2: 2, 3: 1})
print(count[1])   # 3
print(count[999])   # 0