from collections import defaultdict


# 普通字典
normal_dict = {}
print(normal_dict.get('key', 0))   # 需要手动设置默认值

# defaultdict
dd = defaultdict(int)
print(dd['key'])

"""
核心区别：

普通字典：访问不存在的 key 会报错 KeyError

defaultdict：访问不存在的 key 会自动创建，并赋予默认值
"""