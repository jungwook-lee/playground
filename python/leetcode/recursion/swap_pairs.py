import node as nd


def swap(head):
    if head == None:
        return None
    elif head.next == None:
        return head

    n_node = head.next

    # Swap node head and next
    head.next = swap(head.next.next)
    n_node.next = head
    return n_node


if __name__ == '__main__':
    c_node = nd.make_node([i for i in range(8)])
    c_node = swap(c_node)
    print(nd.get_data(c_node))