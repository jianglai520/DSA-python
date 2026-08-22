# python中enumerate函数--返回一个enumerate对象（迭代器），每次迭代会生成一个包含 索引和元素值的元组
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
enumerate每次返回(索引，元素）
"""