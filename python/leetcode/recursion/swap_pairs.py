class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


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


def make_node(i):
    if i == 0:
        return Node(0, None)
    return Node(i, make_node(i - 1))

if __name__ == '__main__':
    c_node = make_node(8)
    c_node = swap(c_node)
    while c_node != None:
        print(c_node.data)
        c_node = c_node.next