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
        self.head = None
        self.__build(self.head, 0, x)

    def __build(self, head, i, x):
        # Exit when list is too big
        if i >= len(x):
            return 
        # Add the new node
        new_node = TreeNode(x[i])
        head = new_node
        
        # Insert insert left, right
        self.__build(new_node.left, (i*2)+1, x)
        self.__build(new_node.right, (i*2)+2, x)

    def print_tree(self):
        if self.head is None:
            print ("Tree is empty!")
            
        def print_h(head):
            if head is None:
                return
            else:
                print(head.val)
                print_h(head.left)
                print_h(head.right)

        return print_h(self.head)

def isSubtree(self, s, t):
    pass

if __name__ == '__main__':
    test = [1,2,3,4]
    new = Tree(test)
    print(new)
    new.print_tree()
