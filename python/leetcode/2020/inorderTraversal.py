from tree import TreeNode, Tree

# Recursive Method
""" Time Complexity O(n), since
    need to visit every node at once

    Space Complexity O(n), at worst
    due to skewed tree, and O(logn)
    average
"""
def inorderTraversal_recursive(root):
    out = []
    def helper(root, out):
        if not root:
            return
        helper(root.left, out)
        out.append(root.val)
        helper(root.right, out)
    helper(root, out)
    return out

""" Time O(n), Space O(n) """
# Iterative Method
def inorderTraversal_iterative(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

if __name__ == '__main__':
    tree = Tree([1, None, 2, None, None, 3])
    print(inorderTraversal_recursive(tree.head))
    print(inorderTraversal_iterative(tree.head))
