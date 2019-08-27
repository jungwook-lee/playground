class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node(%r)' % self.data

def print_list(list):
    cur = list
    while cur != None:
        print(cur)
        cur = cur.next
    print