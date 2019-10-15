def in_order_print(root):
    if root:
        in_order_print(root.left)
        print(root.data)
        in_order_print(root.right)


def pre_order_print(root):
    if root:
        print(root.data)
        pre_order_print(root.left)
        pre_order_print(root.right)


def post_order_print(root):
    if root:
        post_order_print(root.left)
        post_order_print(root.right)
        print(root.data)


def get_max_depth(root, depth=0):
    if root:
        l_depth = get_max_depth(root.left, depth+1)
        r_depth = get_max_depth(root.right, depth+1)
        if l_depth >= r_depth:
    	    return l_depth
        else:
            return r_depth
    else:
        return depth-1


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self, level=0):
        ret = "--"*level + str(self.data) + "\n"
        if self.left:
            ret += self.left.__str__(level+1)
        if self.right:
            ret += self.right.__str__(level+1)
        return ret


if __name__ == '__main__':
    root = Node(5, Node(3), Node(2))
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(10)

    print("In order print")
    in_order_print(root)
    print("Pre order print")
    pre_order_print(root)
    print("Post order print")
    post_order_print(root)
