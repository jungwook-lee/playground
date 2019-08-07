# python implementation of a stack with a linked list (ADT)
class Stack(object):

    # Note that this should be a private object not used by app
    # Internal Node object for stacks
    class Node(object):
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def push(self, item):
        cur_node = self.Node(item, self.head)
        self.head = cur_node

    def pop(self):
        if self.head is None:
            raise Exception('Empty Stack')
        ret_val = self.head.data
        self.head = self.head.next
        return ret_val

    def peek(self):
        if self.head is None:
            raise Exception('Empty Stack')
        return self.head.data

    def isEmpty(self):
        if self.head is None:
            return True
        return False

if __name__ == '__main__':
    st = Stack()
    st.push(1)
    print(st.peek())
    st.push(2)
    st.push(3)
    print(st.peek())
    print(st.isEmpty())
    print(st.pop())
    print(st.pop())
    st.pop()
    print(st.isEmpty())
