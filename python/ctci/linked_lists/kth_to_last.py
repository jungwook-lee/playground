from python.data_structure.node import Node
from python.data_structure.node import print_list

def kth_to_last(k, head):
    count = 0
    front, back = head, head
    while front is not None:
        if count >= k:
            back = back.next
        front = front.next
        count += 1
    if count < k:
        return None
    return back

if __name__ == '__main__':
    node_3 = Node(3)
    node_2 = Node(2, node_3)
    node_1 = Node(1, node_2)
    print_list(node_1)

    print(kth_to_last(2, node_1))
    print(kth_to_last(1, node_1))
    print(kth_to_last(3, node_1))
    print(kth_to_last(4, node_1))