"""
注意：
input()返回的永远是字符串，input()的含义是调用函数，需要等待输入
input的含义是调用对象本身，无需等待输入，返回值是函数对象本身
"""

print(input)    # <built-in function input>
print(type(input))   # <class 'builtin-function-or-method'>

name = input("请输入你的名字:")
print(name)


# 总结：不带括号是函数本身，带括号是“执行函数”