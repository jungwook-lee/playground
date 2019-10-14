from TreeNode import *

def maxDepth(root):
    if root.left:
        l_val = maxDepth(root.left) + 1
    if root.right:
        r_val = maxDepth(root.right) + 1
    if root.left is None and root.right is None:
        return 1

    if l_val > r_val:
        return l_val
    else:
        return r_val


if __name__ == '__main__':
    test_list = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(0)
    arr_to_tree(root, test_list)

    print(maxDepth(root))
