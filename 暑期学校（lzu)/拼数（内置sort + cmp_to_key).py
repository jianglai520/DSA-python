from functools import cmp_to_key

n = int(input())
nums = input().split()

def compare():
    if x + y > y + x:
        return -1
    elif y + x > x + y:
        return 1
    else:
        return 0

nums = sorted(nums, key = cmp_to_key(compare))
print(nums)


# 注意：cmp_to_key用的比较函数里面，返回值如果是负数，代表第一个参数排前面；返回值为0，两个参数相等，顺序无所谓；返回值为正数，第一个参数排后面