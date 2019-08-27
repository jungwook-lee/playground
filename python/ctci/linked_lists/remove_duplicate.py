from python.data_structure.node import Node
from python.data_structure.node import print_list

def remove_dups(list):
    # Early Exit if invalid list
    if list is None:
        return

    hash = dict()
    hash[list.data] = True

    prev, cur = list, list.next
    while cur is not None:
        # Check if data exist in the hash
        if cur.data in hash:
            # Delete from the list
            prev.next = cur.next
            cur = cur.next
        else:
            hash[cur.data] = True
            cur = cur.next
            prev = prev.next

if __name__ == '__main__':
    # 1 -> 2 -> 3 -> 1 -> None
    node_6 = Node(3)
    node_5 = Node(2, node_6)
    node_4 = Node(1, node_5)
    node_3 = Node(3, node_4)
    node_2 = Node(2, node_3)
    node_1 = Node(1, node_2)
    print_list(node_1)

    remove_dups(node_1)
    print_list(node_1)