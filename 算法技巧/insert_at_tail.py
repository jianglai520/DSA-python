from create_linked_list import ListNode, create_linked_list
from print_linked_list import print_linked_list


def insert_at_tail(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node

    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_node
    return head

if __name__ == "__main__":
    head = create_linked_list([2, 3, 4])
    head = insert_at_tail(head, 5)
    print_linked_list(head)