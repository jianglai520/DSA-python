# python中的哈希表实现
# 字典
# 创建字典
d = {}  # 空字典
d = dict()  # 另一种方式

# 添加/修改
d["name"] = "小明"  # 添加
d["age"] = 18
d["age"] = 19  # 修改

# 访问
print(d["name"])  # 小明
print(d.get("score", 0))  # 安全访问，不存在返回0

# 删除
del d["age"]

# 遍历
for key, value in d.items():
    print(f"{key}: {value}")


# 集合只有键，没有值
s = {1, 2, 3, 4, 5}
s.add(6)
s.remove(3)
print(2 in s)  # True，查找也是O(1)