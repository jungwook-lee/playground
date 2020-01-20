import node as nd

# # O(n^2) solution, very bad
# def reverseList(head):
#     # base case
#     if head.next == None:
#         return head
#     new_head = reverseList(head.next)
#
#     # Place the current node to the end
#     temp = new_head
#     while temp.next != None:
#         temp = temp.next
#     temp.next = head
#     head.next = None
#     return new_head

# Runtime O(n), Space O(n)
def reverseList(head):
    if not head:
        return

    if head.next == None:
        return head

    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Iterative Solution O(1), Space of O(1)
def reverseList_iter(head):
    next = head.next
    head.next = None
    while next != None:
        cur = next
        next = next.next
        cur.next = head
        head = cur
    return head

if __name__ == '__main__':
    c_node = nd.make_node([0, 1, 2, 3])
    c_node = reverseList(c_node)
    print(nd.get_data(c_node))

    c_node = nd.make_node(3)
    c_node = reverseList_iter(c_node)
    print(nd.get_data(c_node))