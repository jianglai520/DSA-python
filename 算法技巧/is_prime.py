"""
何为素数：大于1的自然数中，除了1和它本身除外，不再有其他因数的数
"""

# 检查素数
def is_prime(num):
    if num < 2:
        print(f"{num}不是素数")

    i = 2
    while i < num:
        if num % i == 0:
            print(f"{num}不是素数")
            break
        i += 1
    else:
        print(f"{num}是素数")

is_prime(4)
is_prime(5)
is_prime(2)