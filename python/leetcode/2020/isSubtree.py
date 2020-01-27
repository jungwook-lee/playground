class TreeNode(object):
    def __repr__(self):
        return "<TreeNode {}>".format(self.val)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __repr__(self):
        return "<Tree {}>".format(id(self.head))

    def __init__(self, x):
        """ Construct a tree from a heap """
        if not isinstance(x, list):
            raise TypeError('must be a list')
        self.head = self.__build(0, x)

    def __build(self, i, x):
        # Exit when list is too big
        if i >= len(x):
            return None
        # Add the new node
        new_node = TreeNode(x[i])
        # Insert insert left, right
        new_node.left = self.__build((i*2)+1, x)
        new_node.right = self.__build((i*2)+2, x)
        return new_node

    def print_tree(self):
        """ Simple In-order Print of a Tree object """
        if self.head is None:
            print ("Tree is empty!")
            
        def print_h(head):
            if head is None:
                return
            else:
                print(head)
                print_h(head.left)
                print_h(head.right)

        return print_h(self.head)

def isSubtree(self, s, t):
    pass

def isMatch(s,t):
    if (s is None and t is not None) or (s is not None and t is None):
        return False
    elif s is None and t is None:
        return True
    return s.val == t.val and isMatch(s.left, t.left) \
                          and isMatch(s.right, t.right)

def isSubtree(s, t):
    if isMatch(s, t):
        return True
    if not s:
        return False
    return isSubtree(s.left, t) or isSubtree(s.right, t)

if __name__ == '__main__':
    s_in=[4, 1, 2, 4, None, None, None, 1]
    s = Tree(s_in)

    t_in=[4, 1]
    t = Tree(t_in)

    print(isSubtree(s.head, t.head))
