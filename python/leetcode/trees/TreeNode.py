class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def in_order_print(root):
    if root:
        in_order_print(root.left)
        print(root.val)
        in_order_print(root.right)

def arr_to_tree(root, arr, i=0):
    if root is None:
        return
    if i == 0:
        root.val = arr[0]

    # Populate left child
    if left(i) < len(arr):
        l_val = arr[left(i)]
        if l_val is not None:
            root.left = TreeNode(arr[2*i + 1])

    # Populate right child
    if right(i) < len(arr):
        r_val = arr[right(i)]
        if r_val is not None:
            root.right = TreeNode(arr[2*i + 2])

    # Recursive cases
    arr_to_tree(root.left, arr, i+1)
    arr_to_tree(root.right, arr, i+2)

if __name__ == '__main__':
    test_list = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(0)

    arr_to_tree(root, test_list)
    in_order_print(root)
