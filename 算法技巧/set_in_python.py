# 关于python中的集合基本介绍

# a = set()
# a.add((1, 2, 3))
# print(a)
#
# a.add((2, 3, 4))
#
# res = [list(i) for i in a]
# print(res)


# 创建集合的几种方式
s1 = {1, 2, 3}   # 注意： {}是字典，不是空集合
s2 = set()   # 空集合只能这样创建
s3 = set([1, 2, 3, 2, 4, 1])   # 从可迭代对象创建，自动去重
s4 = set("hello")  # 字符串会被拆成字符
s5 = {x * x for x in range(5)}  # 集合推导式
s6 = set(range(5))


