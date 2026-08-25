class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

# 遍历链表
def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end = " -> ")
        cur = cur.next
    print("None")


# 将列表转换为链表
def create_linked_list(arr):
    if not arr:
        return None

    dummy = ListNode()
    cur = dummy

    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    head = create_linked_list(arr)
    print_linked_list(head)

