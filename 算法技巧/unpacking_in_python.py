"""
这个过程发生了什么？
第一次循环：从列表中取出 (0, 1)

解包：把这个元组拆开，0 赋给 row，1 赋给 col

执行循环体
"""
zero_positions = [(0, 1), (2, 3), (3, 4)]

for row, col in zero_positions:
    print(row, col)