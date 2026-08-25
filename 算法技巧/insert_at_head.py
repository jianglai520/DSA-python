# 在链表头部插入节点
from create_linked_list import ListNode, create_linked_list
from 算法技巧.print_linked_list import print_linked_list


def insert_at_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# 测试
if __name__ == "__main__":
    head = create_linked_list([2, 3, 4])
    head = insert_at_head(head, 1)
    print_linked_list(head)
