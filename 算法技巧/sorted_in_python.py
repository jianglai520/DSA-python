"""
sorted()是一个python中的内置函数，用于对可迭代对象进行排序，返回一个新的排序后的列表，不会修改原来的对象
基本语法：
sorted(iterable, *, key = None, reverse = False)
iterable:要排序的可迭代对象(list,tuple, str, dict, set)
key:排序依据的函数，默认为None
reverse:False升序（默认），反之降序

sorted() vs sort()
sorted() 使用于任意的可迭代对象 list.sort() 仅仅适用于列表
sorted() 返回值生成新的列表，而list.sort()则是原地修改，无返回值（None）
sorted() 原对象不变，而list.sort()原对象被修改
"""

# 基本用法
nums = [1, 4, 2, 0, -1, 3, 5, 333333333]
print(sorted(nums))
print(nums)   # 原对象不变

print(sorted(nums, reverse = True))   # 降序排列

print(sorted("python"))  # 返回字符串列表

print(sorted((6, 4, 5)))   # 返回排序列表
print(sorted({9, 4, 5}))   # 返回排序列表


# 使用key参数
words = ["banana", "pie", "apple", "hi"]
print(sorted(words))

print(sorted(words, key=len))   # key 关键字为字符串的长度

nums = [-5, 3, 2, 0, 9, -1, -4]
print(sorted(nums, key = abs))  # 按照绝对值排序

words = ["Banana", "apple", "Cherry"]
print(sorted(words, key = str.lower))   # 忽略大小写排序


# 对字典排序
d = {"banana": 3, "apple": 1, "cherry": 2}

print(sorted(d.items(), key = lambda x: x[0]))  # 按照键排序
print(sorted(d.items(), key = lambda x: x[1]))  # 按照值排序
print(sorted(d))   # 只排序键


