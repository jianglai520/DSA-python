# 遍历链表
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end = " -> ")
        cur = cur.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3)))
print_linked_list(head)