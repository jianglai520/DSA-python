# 字典的get()方法

d = {'a': 1, 'b': 2}

print(d.get('a', 0))  # key存在 --> 返回对应的值

print(d.get('c', 0))  # key不存在 --> 返回默认值

print(d.get('c'))   # 如果不给默认值，key不存在则返回None