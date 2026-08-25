"""
while...else是python特有的语法

while...else 的工作机制

while 条件:
    # 循环体
    if 某个条件:
        break
else:
    # 当循环正常结束（没有执行 break）时执行

"""

# 举例1：在列表中查找元素是否存在
def find_element(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            print(f"找到{target},索引为{i}")
            break
        i += 1
    else:
        print(f"未找到{target}")

# 测试
find_element([1, 2, 3, 4, 5, 6], 3)
find_element([1, 2, 3], 5)


