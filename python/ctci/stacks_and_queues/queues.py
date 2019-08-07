# python implementation of a queue with a linked list (ADT)
class Queue(object):

    class Node(object):
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        # First item case. Both should point to the same object
        new_node = self.Node(item, None)
        if self.first is None and self.last is None:
            self.first, self.last = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def remove(self):
        if self.first is None:
            raise Exception('Queue Empty')

        # When first and last meet
        ret_val = self.first.data
        if self.first is self.last:
            self.first, self.last = None, None
        else:
            self.first = self.first.next
        return ret_val


    def peek(self):
        if self.first is None:
            raise Exception('Queue Empty')
        return self.first.data

    def isEmpty(self):
        if self.first is None:
            return True
        return False

if __name__ == '__main__':
    q = Queue()
    q.add(1)
    print(q.peek())
    q.add(2)
    q.add(3)
    print(q.peek())
    print(q.isEmpty())
    print(q.remove())
    print(q.remove())
    print(q.remove())
    print(q.isEmpty())
