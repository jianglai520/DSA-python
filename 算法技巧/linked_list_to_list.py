from create_linked_list import ListNode, create_linked_list

# 将链表转换为列表
def linked_list_to_list(head):
    result = []
    cur = head

    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


# 使用
head = create_linked_list([1, 2, 3])
print(linked_list_to_list(head))