"""
该文件主要解释在刷题和算法竞赛中，sys用的最多的输入输出加速和递归深度调整
"""

# 最常用 sys.stdin -- 快速读取输入
import sys

data = sys.stdin.read().split()   # 如何结束：ctrl + D
print(data)


"""
data = sys.stdin.buffer.read().split() 少一步解码，运行更快一点，结果和sys.stdin.read().split()完全一样

sys.stdin.readline() 比input()快，但还是需要一行一行读
"""
