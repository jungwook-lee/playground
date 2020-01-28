from tree import TreeNode, Tree

""" Runtime would be O(m) where m is
    the number of nodes. It would have
    to traverse through every single node.

    Worst case would be O(n), average
    O(log n).
"""
def invertTree(root):
    if root is None:
        return root
    # base case
    temp = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(temp)
    return root

if __name__ == '__main__':
    tree = Tree([4,2,7,1,3,6,9])
    out = invertTree(tree.head)
    out_Tree = Tree([])
    out_Tree.head = out
    out_Tree.print_tree()
