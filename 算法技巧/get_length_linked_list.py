from create_linked_list import  create_linked_list

def get_length_linked_list(head):
    count = 0
    cur = head

    while cur:
        count += 1
        cur = cur.next
    return count

if __name__ == "__main__":
    head = create_linked_list([1, 2, 3])
    print(get_length_linked_list(head))
