from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head

    pre = dummy
    start = head

    while True:
        end = pre
        for _ in range(k):
            end = end.next
            if not end:
                return dummy.next

        next_group = end.next
        end.next = None

        new_head = reverse(start)

        pre.next = new_head
        start.next = next_group

        if not start:
            return dummy.next

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev