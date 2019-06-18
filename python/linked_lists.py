class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return

        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next


class Node(object):
    def __init__(self, num):
        self.data = num
        self.next = None


if __name__ == "__main__":
    # Test the classes
    ll = LinkedList()

    node1 = Node(5)
    node2 = Node(10)
    node3 = Node(4)

    ll.head = node1
    node1.next = node2
    node2.next = node3

    ll.print_list()