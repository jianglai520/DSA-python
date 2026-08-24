"""
数组：像电影院的一排座位，每个人有固定编号，坐在一起
链表：像“寻宝游戏”，每个节点告诉你“我是谁？”和“下一个线索在哪”
"""

# 定义链表
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val  # 节点存储的值
        self.next = next # 指向下一个节点的指针

"""
val：这个节点存的数据（可以是任意类型）
next：指向下一个ListNode对象，如果没有下一个就是None
"""

# 创建单个节点
node1 = ListNode(5)
print(node1.val)  # 5
print(node1.next) # None


# 创建多个节点并连接
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

# 现在链表是： 1 -> 2 -> 3

