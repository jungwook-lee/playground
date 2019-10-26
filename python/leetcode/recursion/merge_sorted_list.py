import node as nd


def mergeTwoLists(list1, list2):
    """ Returns a merged list that is spliced from inputs """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        node = list1
        out = mergeTwoLists(list1.next, list2)
    else:
        node = list2
        out = mergeTwoLists(list1, list2.next)

    node.next = out
    return node


if __name__ == '__main__':
    list1 = nd.make_node([1, 2, 4])
    list2 = nd.make_node([1, 3, 4])
    print(nd.get_data(mergeTwoLists(list1, list2)))

    list1 = nd.make_node([])
    list2 = nd.make_node([0])
    print(nd.get_data(mergeTwoLists(list1, list2)))

    list1 = nd.make_node([2])
    list2 = nd.make_node([1])
    print(nd.get_data(mergeTwoLists(list1, list2)))