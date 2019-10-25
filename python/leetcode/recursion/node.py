class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def make_node(node_list):
    """ Given a list of values, makes a linked list, supports single int or list """
    if type(node_list) is int:
        node_list = [node_list]
    if len(node_list) <= 1:
        return Node(node_list[0], None)
    return Node(node_list[0], make_node(node_list[1:]))

def get_data(head):
    """ Returns a list of values of the linked list """
    out = []
    while head is not None:
        out.append(head.data)
        head = head.next
    return out

if __name__ == '__main__':
    test_list = [1, 2, 3, 4]
    node_list = make_node(node_list=test_list)
    assert(test_list == get_data(node_list))
