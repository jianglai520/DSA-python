# isdigit() 是python中字符串的一个内置方法，用于判断字符串是否只包含数字字符

print("123".isdigit())  # True
print("h123".isdigit()) # False

print("-123".isdigit())   # False  注意：不能判断负数或小数

print("²".isdigit())  # True 注意：Unicode数字也支持

print("".isdigit())   # False 注意：空字符串返回False